import streamlit as st
from analytics import moving_average, pct_change

st.title("Dashboard Financeiro")
symbol = st.selectbox("Símbolo", ["ABC", "DEF", "GHI"])
window = st.slider("Janela MA (dias)", 5, 60, 20)
ma = moving_average(symbol, window)
pc = pct_change(symbol, 1)
st.metric("Média Móvel", f"{ma:.2f}")
st.metric("Variação % (dia)", f"{pc:.2f}%")

