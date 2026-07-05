import os

import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv

from agent import aggregate_by_category, categorize_transactions, generate_roast
from parser import parse_csv, parse_pdf

load_dotenv()

st.set_page_config(page_title='RoastMyExpenses', page_icon='💸', layout='wide')

st.title('💸 RoastMyExpenses')
st.caption('Upload your bank statement. Get roasted.')

if not os.getenv('ANTHROPIC_API_KEY'):
    st.error('ANTHROPIC_API_KEY is not set. Add it to your .env file and restart.')
    st.stop()

uploaded = st.file_uploader(
    'Upload bank statement (CSV recommended, PDF best-effort)',
    type=['csv', 'pdf'],
)

if uploaded is None:
    st.info('CSV export from your bank portal gives the most reliable results.')
    st.stop()

file_bytes = uploaded.read()
ext = uploaded.name.rsplit('.', 1)[-1].lower()

transactions: pd.DataFrame | None = None
pdf_low_confidence = False

with st.spinner('Parsing statement…'):
    try:
        if ext == 'csv':
            transactions = parse_csv(file_bytes)
        else:
            transactions, high_confidence = parse_pdf(file_bytes)
            pdf_low_confidence = not high_confidence
    except ValueError as exc:
        st.error(str(exc))
        st.stop()

if pdf_low_confidence:
    st.warning(
        '⚠️ PDF extraction confidence is low — your bank\'s layout may not be '
        'fully supported. Results may be incomplete. Try exporting as CSV instead.'
    )

if transactions is None or transactions.empty:
    st.error('No transactions found. Try a CSV export from your bank portal.')
    st.stop()

transactions = categorize_transactions(transactions)
category_totals = aggregate_by_category(transactions)

st.success(f'Parsed **{len(transactions)}** transactions across **{len(category_totals)}** categories.')

left, right = st.columns([1, 1], gap='large')

with left:
    st.subheader('Spending Breakdown')

    chart_df = category_totals.reset_index()
    chart_df.columns = ['Category', 'Amount']

    fig = px.bar(
        chart_df,
        x='Amount',
        y='Category',
        orientation='h',
        color='Amount',
        color_continuous_scale='RdYlGn_r',
        labels={'Amount': f'Amount ({chr(8377)})'},
    )
    fig.update_layout(
        showlegend=False,
        coloraxis_showscale=False,
        yaxis={'categoryorder': 'total ascending'},
        margin={'l': 0, 'r': 0, 't': 0, 'b': 0},
    )
    st.plotly_chart(fig, use_container_width=True)

    display_df = chart_df.copy()
    display_df['Amount'] = display_df['Amount'].apply(lambda x: f'₹{x:,.0f}')
    st.dataframe(display_df, use_container_width=True, hide_index=True)

with right:
    st.subheader('Your Roast 🔥')

    if 'roast' in st.session_state:
        st.markdown(
            f"""<div style="background:#1a1a2e;border-left:4px solid #ff4b4b;
            padding:1.4rem 1.6rem;border-radius:8px;color:#f0f0f0;
            font-size:1.05rem;line-height:1.75;white-space:pre-wrap;">{st.session_state['roast']}</div>""",
            unsafe_allow_html=True,
        )
        if st.button('Roast me again 🔁'):
            del st.session_state['roast']
            st.rerun()
    else:
        if st.button('Roast Me 🔥', type='primary'):
            roast_text = st.write_stream(generate_roast(category_totals))
            st.session_state['roast'] = roast_text
            st.rerun()
