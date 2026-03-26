import streamlit as st
import pandas as pd

st.set_page_config(page_title="Radar de Preços Aju", page_icon="📡")

# LOGO SVG (Aquele que criamos)
st.markdown('<div style="text-align:center"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 150" width="200"><circle cx="75" cy="75" r="70" fill="#004a99"/><text x="170" y="80" font-family="Arial" font-size="40" font-weight="bold" fill="#003366">radar<tspan fill="#ff7f00">aju</tspan></text></svg></div>', unsafe_allow_html=True)

st.title("📡 Radar de Preços - Aracaju")

# BANNER LGPD
if 'aceito' not in st.session_state:
    if st.button("Aceitar Termos e Cookies (LGPD)"):
        st.session_state['aceito'] = True

# BUSCA
busca = st.text_input("O que você procura hoje em Aracaju?")

try:
    df = pd.read_csv("dados_precos.csv")
    if busca:
        df = df[df['produto'].str.contains(busca, case=False)]
    st.table(df)
except:
    st.info("Aguardando primeira coleta de dados do robô...")

# RODAPÉ LEGAL
st.markdown("---")
st.caption("© 2026 Radar de Preços Aju - Uso Informativo - Polícia Civil/Sindicato SE")
