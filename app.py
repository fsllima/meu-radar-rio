import streamlit as st
import datetime
import pytz

# Configuração da página
st.set_page_config(page_title="Radar Motorista RJ", page_icon="🚖", layout="centered")

def obter_hora_rio():
    fuso_rio = pytz.timezone('America/Sao_Paulo')
    return datetime.datetime.now(fuso_rio)

# Estilo Personalizado para parecer um App
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #000; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚖 Radar de Demanda RJ")
st.subheader("Inteligência para Motoristas")

agora = obter_hora_rio()
hora = agora.hour

st.info(f"📅 {agora.strftime('%d/%m/%Y')} | ⏰ {agora.strftime('%H:%M')}")

# --- SEÇÃO 1: AEROPORTOS ---
st.header("✈️ Aeroportos (GIG/SDU)")
col1, col2 = st.columns(2)
with col1:
    st.link_button("Painel Galeão (Ao Vivo)", "https://www.riogaleao.com/passageiros/voos/painel-de-voos")
with col2:
    st.link_button("Painel SDU (Infraero)", "https://www.infraero.gov.br/voos/index.aspx")

if (8 <= hora <= 11) or (19 <= hora <= 23):
    st.warning("🔥 PICO DE POUSOS: Grande volume de chegadas agora!")

# --- SEÇÃO 2: HOTÉIS (CHECK-OUT) ---
st.header("🏨 Hotéis (Check-out)")
if 10 <= hora < 13:
    st.success("💰 HORA DE OURO: Check-out na Zona Sul e Barra.")
    st.write("📍 **Foco:** Orla de Copacabana e Hotéis da Barra/Recreio.")
else:
    st.write("🕒 Fora do horário de pico de hotéis (10h30 - 12h30).")

# --- SEÇÃO 3: RODOVIÁRIA ---
st.header("🚌 Rodoviária Novo Rio")
if 5 <= hora <= 9:
    st.success("🚨 CHEGADAS RODOVIÁRIA: Fluxo intenso de passageiros.")
else:
    st.write("Movimento normal na Rodoviária.")

# --- SEÇÃO 4: EVENTOS ---
st.header("🎭 Eventos e Lazer")
st.link_button("Agenda de Eventos RJ (Visit.Rio)", "https://visit.rio/eventos/")

st.divider()
st.caption("Versão 1.0 - Use para planejar suas rotas.")
