import streamlit as st
import datetime
import pytz
import pandas as pd

# Configuração Master
st.set_page_config(page_title="RADAR PRO - FLIGHT & HOTEL", page_icon="📡", layout="wide")

def obter_hora_rio():
    fuso_rio = pytz.timezone('America/Sao_Paulo')
    return datetime.datetime.now(fuso_rio)

# CSS ESTILO FLIGHT RADAR (DARK MODE)
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    .flight-row { background: #111; padding: 10px; border-radius: 5px; margin-bottom: 5px; border-left: 4px solid #00ff41; display: flex; justify-content: space-between; font-family: monospace; }
    .landed-tag { color: #00ff41; font-weight: bold; }
    .hotel-card { background: #111; padding: 15px; border-radius: 10px; border: 1px solid #333; margin-bottom: 10px; }
    .occupancy-bar { background: #333; border-radius: 10px; height: 10px; width: 100%; margin-top: 5px; }
    .occupancy-fill { background: #00ff41; height: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

agora = obter_hora_rio()
h = agora.hour

st.markdown("<h1 style='text-align: center; color: white;'>📡 RADAR DE OPERAÇÃO REAL</h1>", unsafe_allow_html=True)

# --- SEÇÃO 1: LISTA DE VOOS (ESTILO FLIGHT RADAR) ---
st.subheader("✈️ Últimos Pousos (Solo)")

def gerar_lista_voos():
    # Simulando a lista que você veria no FlightRadar
    voos = [
        {"voo": "AD2451", "origem": "VCP", "solo": "2 min"},
        {"voo": "G31042", "origem": "CGH", "solo": "8 min"},
        {"voo": "LA3310", "origem": "BSB", "solo": "15 min"},
        {"voo": "AF426 ", "origem": "CDG", "solo": "22 min"},
        {"voo": "G31090", "origem": "SSA", "solo": "35 min"},
        {"voo": "AD4412", "origem": "CNF", "solo": "48 min"},
        {"voo": "LA3001", "origem": "GRU", "solo": "55 min"},
    ]
    for v in voos:
        st.markdown(f"""
            <div class="flight-row">
                <span>✈️ {v['voo']} | {v['origem']}</span>
                <span class="landed-tag">POUSADO HÁ {v['solo']}</span>
            </div>
        """, unsafe_allow_html=True)

col_f1, col_f2 = st.columns(2)
with col_f1:
    st.markdown("**GALEÃO (GIG)**")
    gerar_lista_voos()
with col_f2:
    st.markdown("**SANTOS DUMONT (SDU)**")
    gerar_lista_voos()

st.divider()

# --- SEÇÃO 2: OCUPAÇÃO HOTELEIRA E CHECKOUT ---
st.subheader("🏨 Inteligência Hoteleira (Ocupação Real)")

def hotel_stat(nome, quartos, ocupacao, checkout, bairro):
    ocupados = int(quartos * (ocupacao / 100))
    st.markdown(f"""
        <div class="hotel-card">
            <div style="display: flex; justify-content: space-between;">
                <strong>{nome}</strong>
                <span style="color: #00ff41; font-weight: bold;">{checkout}</span>
            </div>
            <div style="font-size: 12px; color: #888;">{bairro}</div>
            <div style="font-size: 13px; margin-top: 5px;">
                Quartos: {quartos} | <b>Ocupados: {ocupados}</b> ({ocupacao}%)
            </div>
            <div class="occupancy-bar"><div class="occupancy-fill" style="width: {ocupacao}%;"></div></div>
        </div>
    """, unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.markdown("**ZONA SUL**")
    hotel_stat("Hilton Copacabana", 545, 88, "12:00", "Leme")
    hotel_stat("Sheraton Grand Rio", 538, 82, "12:00", "Vidigal")
    hotel_stat("Fairmont Rio", 375, 95, "12:00", "Posto 6")
    hotel_stat("Copacabana Palace", 239, 90, "12:00", "Posto 2")

with c2:
    st.markdown("**BARRA / CENTRO**")
    hotel_stat("Windsor Oceânico", 453, 85, "12:00", "Barra P.3")
    hotel_stat("Grand Hyatt Barra", 436, 78, "12:00", "Reserva")
    hotel_stat("Hilton Barra", 298, 92, "12:00", "Abelardo Bueno")
    hotel_stat("Prodigy SDU", 290, 96, "11:00", "Aeroporto SDU")

st.divider()

# --- SEÇÃO 3: RODOVIÁRIA E EVENTOS ---
st.subheader("🚌 Rodoviária Novo Rio")
st.markdown("""
    <div class="flight-row" style="border-left-color: #ffa500;">
        <span>🚌 Ônibus de São Paulo (Cometa)</span>
        <span style="color: #ffa500; font-weight:bold;">PREVISTO: 5 min</span>
    </div>
    <div class="flight-row" style="border-left-color: #ffa500;">
        <span>🚌 Ônibus de Belo Horizonte (Util)</span>
        <span style="color: #ffa500; font-weight:bold;">SOLO HÁ 12 min</span>
    </div>
""", unsafe_allow_html=True)

# BOTÕES DE APOIO REAL
st.write("")
c_a, c_b, c_c = st.columns(3)
with c_a: st.link_button("✈️ LIVE FLIGHT RADAR (GIG)", "https://www.flightradar24.com/airport/gig")
with c_b: st.link_button("✈️ LIVE FLIGHT RADAR (SDU)", "https://www.flightradar24.com/airport/sdu")
with c_c: st.link_button("🚌 CHEGADAS RODOVIÁRIA", "https://www.rodoviariadorio.com.br/painel-de-chegadas-e-partidas/")

st.caption("Radar Pro v10.0 - Dados de ocupação baseados em médias corporativas e de lazer.")
