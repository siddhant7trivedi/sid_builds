import os
from typing import Generator

import anthropic
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

CATEGORY_RULES: dict[str, str] = {
    # Food Delivery
    'SWIGGY': 'Food Delivery',
    'ZOMATO': 'Food Delivery',
    'DUNZO': 'Food Delivery',
    'MAGICPIN': 'Food Delivery',

    # Groceries
    'BIGBASKET': 'Groceries',
    'GROFERS': 'Groceries',
    'BLINKIT': 'Groceries',
    'JIOMART': 'Groceries',
    'ZEPTO': 'Groceries',
    'DMART': 'Groceries',
    'RELIANCE FRESH': 'Groceries',
    'MORE SUPERMARKET': 'Groceries',
    'SUPERMARKET': 'Groceries',

    # Dining Out
    'RESTAURANT': 'Dining Out',
    'CAFE': 'Dining Out',
    'COFFEE': 'Dining Out',
    'BISTRO': 'Dining Out',
    'PIZZA': 'Dining Out',
    'BURGER': 'Dining Out',
    'KFC': 'Dining Out',
    'MCDONALD': 'Dining Out',
    'DOMINO': 'Dining Out',
    'SUBWAY': 'Dining Out',
    'STARBUCKS': 'Dining Out',
    'CCD': 'Dining Out',
    'BARISTA': 'Dining Out',
    'CHAAYOS': 'Dining Out',
    'HALDIRAM': 'Dining Out',

    # Online Shopping
    'AMAZON': 'Online Shopping',
    'FLIPKART': 'Online Shopping',
    'MYNTRA': 'Online Shopping',
    'NYKAA': 'Online Shopping',
    'MEESHO': 'Online Shopping',
    'AJIO': 'Online Shopping',
    'SNAPDEAL': 'Online Shopping',
    'TATACLIQ': 'Online Shopping',
    'CROMA': 'Online Shopping',
    'RELIANCE DIGITAL': 'Online Shopping',
    'SHOPIFY': 'Online Shopping',

    # Subscriptions & Entertainment
    'NETFLIX': 'Subscriptions',
    'PRIME VIDEO': 'Subscriptions',
    'AMAZON PRIME': 'Subscriptions',
    'SPOTIFY': 'Subscriptions',
    'HOTSTAR': 'Subscriptions',
    'DISNEY': 'Subscriptions',
    'ZEE5': 'Subscriptions',
    'SONYLIV': 'Subscriptions',
    'APPLE': 'Subscriptions',
    'YOUTUBE PREMIUM': 'Subscriptions',
    'STEAM': 'Subscriptions',
    'GAMEPASS': 'Subscriptions',

    # Transport
    'OLA': 'Transport',
    'UBER': 'Transport',
    'RAPIDO': 'Transport',
    'METRO': 'Transport',
    'IRCTC': 'Transport',
    'REDBUS': 'Transport',
    'YULU': 'Transport',
    'BOUNCE': 'Transport',

    # Fuel
    'HPCL': 'Fuel',
    'BPCL': 'Fuel',
    'IOCL': 'Fuel',
    'SHELL': 'Fuel',
    'PETROL': 'Fuel',
    'DIESEL': 'Fuel',
    'FUEL': 'Fuel',
    'HP PETRO': 'Fuel',

    # Travel
    'MAKEMYTRIP': 'Travel',
    'GOIBIBO': 'Travel',
    'CLEARTRIP': 'Travel',
    'BOOKING.COM': 'Travel',
    'AIRBNB': 'Travel',
    'INDIGO': 'Travel',
    'AIR INDIA': 'Travel',
    'VISTARA': 'Travel',
    'SPICEJET': 'Travel',

    # Utilities
    'BESCOM': 'Utilities',
    'MSEDCL': 'Utilities',
    'TATA POWER': 'Utilities',
    'ELECTRICITY': 'Utilities',
    'MAHANAGAR GAS': 'Utilities',
    'AIRTEL': 'Utilities',
    'JIO': 'Utilities',
    'VODAFONE': 'Utilities',
    'BSNL': 'Utilities',
    'ACT FIBERNET': 'Utilities',
    'TATA SKY': 'Utilities',
    'BROADBAND': 'Utilities',

    # Health & Wellness
    'MEDPLUS': 'Health & Wellness',
    'APOLLO PHARMACY': 'Health & Wellness',
    '1MG': 'Health & Wellness',
    'PRACTO': 'Health & Wellness',
    'NETMEDS': 'Health & Wellness',
    'CULT.FIT': 'Health & Wellness',
    'CULTFIT': 'Health & Wellness',
    'PHARMACY': 'Health & Wellness',
    'HOSPITAL': 'Health & Wellness',
    'CLINIC': 'Health & Wellness',
    'GYM': 'Health & Wellness',

    # Education
    'BYJU': 'Education',
    'UNACADEMY': 'Education',
    'COURSERA': 'Education',
    'UDEMY': 'Education',
    'SKILLSHARE': 'Education',
    'VEDANTU': 'Education',

    # ATM / Cash
    'ATM': 'ATM/Cash Withdrawal',
    'CASH WITHDRAWAL': 'ATM/Cash Withdrawal',
}


def categorize_transactions(df: pd.DataFrame) -> pd.DataFrame:
    def _match(desc: str) -> str:
        upper = str(desc).upper()
        for keyword, category in CATEGORY_RULES.items():
            if keyword in upper:
                return category
        return 'Other'

    df = df.copy()
    df['category'] = df['description'].apply(_match)
    return df


def aggregate_by_category(df: pd.DataFrame) -> pd.Series:
    return df.groupby('category')['amount'].sum().sort_values(ascending=False)


def generate_roast(category_totals: pd.Series, currency: str = '₹') -> Generator[str, None, None]:
    """Stream a savage roast from Claude given aggregated category totals."""
    totals_text = '\n'.join(
        f"  {cat}: {currency}{amount:,.0f}"
        for cat, amount in category_totals.items()
    )

    prompt = f"""You are a brutally honest, specific, and witty personal finance roast comedian.
You have a person's monthly spending summary. Roast them — hard.

Rules:
- Be SPECIFIC. Reference actual category names and exact amounts.
- Be SAVAGE, not generic. "You spend too much" is worthless. Tie every joke to the actual number.
- For the top 3–5 spending categories, write one sharp roast line each.
- End with exactly one "Next Month's Challenge:" line — one specific change they must make.
- No bullet points, no headers. Flowing prose, then the challenge line.
- Under 300 words total.

Their spending:
{totals_text}

Roast them."""

    client = anthropic.Anthropic()

    with client.messages.stream(
        model='claude-opus-4-8',
        max_tokens=1024,
        messages=[{'role': 'user', 'content': prompt}],
    ) as stream:
        for text in stream.text_stream:
            yield text
