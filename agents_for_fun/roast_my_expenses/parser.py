import re
import io
from typing import Tuple, Optional

import pandas as pd
import pdfplumber

_ACCOUNT_RE = re.compile(r'\b\d{12,18}\b')
_CARD_RE = re.compile(r'\b(?:\d[ -]?){15,16}\b')
_IFSC_RE = re.compile(r'\b[A-Z]{4}0[A-Z0-9]{6}\b')


def mask_sensitive(text: str) -> str:
    text = _ACCOUNT_RE.sub('[ACCT]', text)
    text = _CARD_RE.sub('[CARD]', text)
    text = _IFSC_RE.sub('[IFSC]', text)
    return text


def _normalize_columns(df: pd.DataFrame) -> Optional[pd.DataFrame]:
    df = df.copy()
    df.columns = [str(c).strip().lower() for c in df.columns]

    date_cols = [c for c in df.columns if any(k in c for k in ('date', 'txn date', 'value date', 'posting'))]
    desc_cols = [c for c in df.columns if any(k in c for k in ('narr', 'desc', 'particular', 'remark', 'detail', 'trans'))]
    debit_cols = [c for c in df.columns if any(k in c for k in ('debit', 'withdrawal', 'dr', 'paid'))]
    amt_cols = [c for c in df.columns if any(k in c for k in ('amount', 'amt'))]

    if not desc_cols:
        return None

    amt_col = (debit_cols or amt_cols or [None])[0]
    if amt_col is None:
        return None

    result = pd.DataFrame()
    if date_cols:
        result['date'] = pd.to_datetime(df[date_cols[0]], errors='coerce')
    result['description'] = df[desc_cols[0]].fillna('').astype(str)
    result['amount'] = (
        pd.to_numeric(
            df[amt_col].astype(str)
            .str.replace(',', '', regex=False)
            .str.replace('₹', '', regex=False)
            .str.strip(),
            errors='coerce'
        ).abs()
    )
    result = result[result['amount'].notna() & (result['amount'] > 0)].reset_index(drop=True)
    return result if not result.empty else None


def parse_csv(file_bytes: bytes) -> pd.DataFrame:
    df = None
    for enc in ('utf-8-sig', 'utf-8', 'latin-1'):
        try:
            df = pd.read_csv(io.BytesIO(file_bytes), encoding=enc, on_bad_lines='skip')
            break
        except (UnicodeDecodeError, Exception):
            continue

    if df is None or df.empty:
        raise ValueError("Could not read CSV file.")

    normalized = _normalize_columns(df)
    if normalized is None or normalized.empty:
        raise ValueError(
            "Could not detect transaction columns. "
            "Ensure your CSV has date, description, and debit/amount columns."
        )

    normalized['description'] = normalized['description'].apply(mask_sensitive)
    return normalized


def parse_pdf(file_bytes: bytes) -> Tuple[pd.DataFrame, bool]:
    """Returns (DataFrame, high_confidence). high_confidence=False when extraction looks incomplete."""
    rows = []
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                for table in (page.extract_tables() or []):
                    if table:
                        rows.extend(table)
    except Exception as exc:
        raise ValueError(f"Could not open PDF: {exc}") from exc

    if len(rows) < 3:
        return pd.DataFrame(), False

    header = [str(c).strip() if c else f'col_{i}' for i, c in enumerate(rows[0])]
    data = [r for r in rows[1:] if any(cell for cell in r)]
    df = pd.DataFrame(data, columns=header)

    normalized = _normalize_columns(df)
    if normalized is None or normalized.empty:
        return pd.DataFrame(), False

    normalized['description'] = normalized['description'].apply(mask_sensitive)
    high_confidence = len(normalized) >= 5
    return normalized, high_confidence
