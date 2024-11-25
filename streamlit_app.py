import streamlit as st

col1, col2, col3 = st.columns([2, 7, 1])
with col1:
    currency = st.selectbox("", ["TWD", "RON", "EUR"])
with col2:
    amount = st.number_input("", min_value=0, step=10)

ron_to_twd = 6.84  # 1 RON = 6.84 TWD
eur_to_twd = 34.02  # 1 EUR = 34.02 TWD

if currency == "TWD":
    twd = amount
    lei = amount / ron_to_twd
    eur = amount / eur_to_twd
elif currency == "RON":
    twd = amount * ron_to_twd
    lei = amount
    eur = (amount * ron_to_twd) / eur_to_twd
elif currency == "EUR":
    twd = amount * eur_to_twd
    lei = (amount * eur_to_twd) / ron_to_twd
    eur = amount

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"<p style='font-size:54px; font-weight:bold; margin:0; display:inline;'>{twd:.2f} </p>"
        f"<span style='font-size:20px; font-weight:bold;'>TWD</span>",
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"<p style='font-size:54px; font-weight:bold; margin:0; display:inline;'>{lei:.2f} </p>"
        f"<span style='font-size:20px; font-weight:bold;'>LEI</span>",
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"<p style='font-size:54px; font-weight:bold; margin:0; display:inline;'>{eur:.2f} </p>"
        f"<span style='font-size:20px; font-weight:bold;'>EUR</span>",
        unsafe_allow_html=True,
    )
