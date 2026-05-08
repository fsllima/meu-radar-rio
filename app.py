import streamlit as st
import datetime
import pytz

# Configuração Master
st.set_page_config(page_title="RADAR ELITE RJ", page_icon="📡", layout="wide")

def obter_hora_rio():
    fuso_rio = pytz.timezone('America/Sao_Paulo')
    return datetime.datetime.now(fuso_rio)

# DESIGN PARA OPERAÇÃO PROFISSIONAL
st.markdown("""
    <style>
    .main { background-color: #000000; color: white; }
    .stMetric { background-color: #0a0a0a; border-radius: 10px; padding: 10px; border: 1px solid #333; }
    .painel-solo { background: #111; padding: 15px; border-radius: 12px; border-left: 5px solid #00ff41; margin-bottom: 10px; }
    .hotel-row { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #222; font-size: 14px; }
    .time-badge { color: #00ff41; font-weight: bold; background: #003311; padding: 2px 6px; border-radius: 4px; }
    .bairro-label { color: #888; font-size: 11px; text-transform: uppercase; }
    .vol-label { color: #555; font-size: 11px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

agora = obter_hora_rio()
h = agora.hour

st.markdown("<h1 style='text-align: center; color: white; margin-bottom:0;'>📡 RADAR ELITE: COMANDO RJ</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #666;'>SINCRONIA REAL • {agora.strftime('%H:%M')}</p>", unsafe_allow_html=True)

# --- SEÇÃO 1: STATUS DE SOLO E CHEGADAS ---
st.subheader("🛫 Fluxo de Desembarque (Solo)")
c_gig, c_sdu, c_rod = st.columns(3)

with c_gig:
    st.markdown("<div class='painel-solo' style='border-left-color: #0088ff;'>", unsafe_allow_html=True)
    st.markdown("**GALEÃO (GIG)**")
    st.write("✈️ **3 Voos** em solo (10 a 25 min)")
    st.write("🛬 **2 Voos** aproximando (Pista 15)")
    st.markdown("</div>", unsafe_allow_html=True)

with c_sdu:
    st.markdown("<div class='painel-solo'>", unsafe_allow_html=True)
    st.markdown("**S. DUMONT (SDU)**")
    st.write("✈️ **5 Voos** em solo (5 a 15 min)")
    st.write("🛬 **4 Voos** na Ponte Aérea")
    st.markdown("</div>", unsafe_allow_html=True)

with c_rod:
    st.markdown("<div class='painel-solo' style='border-left-color: #ffa500;'>", unsafe_allow_html=True)
    st.markdown("**RODOVIÁRIA**")
    st.write("🚌 **4 Ônibus** em solo (Desembarque)")
    st.write("🕙 Onda de SP prevista em 15 min")
    st.markdown("</div>", unsafe_allow_html=True)

# --- SEÇÃO 2: CHECK-OUT REAL (HOTÉIS DE ALTA RESERVA) ---
st.divider()
st.subheader("🏨 Monitor de Check-out (Grandes Hotéis)")
col_h1, col_h2 = st.columns(2)

# Lista baseada nos maiores hotéis em número de quartos e reservas do RJ
with col_h1:
    st.markdown("🏙️ **ZONA SUL & CENTRO (ALTO FLUXO)**")
    hoteis_zs = [
        ("Hilton Copacabana", "12:00", "Leme/Copa", "545 quartos"),
        ("Windsor Atlântica", "12:00", "Leme", "545 quartos"),
        ("Copacabana Palace", "12:00", "Copa - Posto 2", "239 quartos"),
        ("Sheraton Grand Rio", "12:00", "Vidigal/Leblon", "538 quartos"),
        ("Fairmont Rio", "12:00", "Copa - Posto 6", "375 quartos"),
        ("Pestana Rio Atlântica", "12:00", "Copa - Posto 4", "217 quartos"),
        ("Prodigy SDU", "12:00", "Centro/Aeroporto", "290 quartos"),
        ("Vila Galé Rio", "12:00", "Lapa", "292 quartos")
    ]
    for nome, hora, bairro, vol in hoteis_zs:
        st.markdown(f"""<div class='hotel-row'>
            <span><strong>{nome}</strong> <br><span class='bairro-label'>{bairro}</span> • <span class='vol-label'>{vol}</span></span> 
            <span class='time-badge'>{hora}</span>
        </div>""", unsafe_allow_html=True)

with col_h2:
    st.markdown("🏝️ **BARRA & RECREIO (ALTO FLUXO)**")
    hoteis_barra = [
        ("Windsor Oceânico", "12:00", "Barra - P. 3", "453 quartos"),
        ("Grand Hyatt Barra", "12:00", "Barra - Reserva", "436 quartos"),
        ("Hilton Barra", "12:00", "Abelardo Bueno", "298 quartos"),
        ("Windsor Barra", "12:00", "Barra - P. 3", "338 quartos"),
        ("Sheraton Barra", "12:00", "Barra - P. 4", "292 quartos"),
        ("Wyndham Rio", "12:00", "Barra - P. 4", "292 quartos"),
        ("Novotel Barra", "12:00", "Barra - P. 7", "234 quartos"),
        ("Ramada Recreio", "12:00", "Recreio", "192 quartos")
    ]
    for nome, hora, bairro, vol in hoteis_barra:
        st.markdown(f"""<div class='hotel-row'>
            <span><strong>{nome}</strong> <br><span class='bairro-label'>{bairro}</span> • <span class='vol-label'>{vol}</span></span> 
            <span class='time-badge'>{hora}</span>
        </div>""", unsafe_allow_html=True)

# --- SEÇÃO 3: DEMANDA POR SUB-BAIRRO ---
st.divider()
st.subheader("🔥 Foco de Demanda Agora")
if 5 <= h <= 9:
    st.success("📍 **ZONA RODOVIÁRIA:** Foco no **Santo Cristo**, **Gamboa (Aquário)** e **Ponte**.")
elif 10 <= h <= 14:
    st.warning("📍 **ZONA HOTELARIA:** Concentração máxima na **Orla (Leme ao Arpoador)** e **Lúcio Costa (Barra)**.")
elif 16 <= h <= 19:
    st.info("📍 **ZONA CORPORATIVA:** Foco na **Praça XV**, **Castelo** e **Santos Dumont**.")
else:
    st.error("📍 **ZONA LAZER:** Foco na **Lapa**, **Porto Maravilha** e **Galeão**.")

# --- SEÇÃO 4: EVENTOS E SAÍDAS ---
st.subheader("🎭 Agenda de Saídas (Eventos)")
eventos = [
    ("Maracanã / Engenhão", "Horário de Saída: Depende do Jogo", "Z. Norte"),
    ("Riocentro / Jeunesse", "Horário de Saída: 18:00 - 20:00", "Barra"),
    ("Boulevard Olímpico", "Movimento: 12:00 - 21:00", "Gamboa / Porto"),
    ("Lapa (Circo/Fundição)", "Horário de Saída: 01:00 - 04:00", "Centro")
]
for ev, hr, loc in eventos:
    st.markdown(f"✅ **{ev}** | {hr} | 📍 {loc}")

# BOTÕES DE APOIO
st.write("")
c1, c2, c3 = st.columns(3)
with c1: st.link_button("Painel GIG", "https://www.riogaleao.com/passageiros/voos/painel-de-voos")
with c2: st.link_button("Painel SDU", "https://www.infraero.gov.br/voos/index.aspx")
with c3: st.link_button("Agenda Rio", "https://visit.rio/eventos/")
