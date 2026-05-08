import streamlit as st
import datetime
import pytz

# Configuração Master
st.set_page_config(page_title="CENTRAL RADAR RJ", page_icon="📡", layout="wide")

def obter_hora_rio():
    fuso_rio = pytz.timezone('America/Sao_Paulo')
    return datetime.datetime.now(fuso_rio)

# CSS PARA INTERFACE DE ALTO IMPACTO
st.markdown("""
    <style>
    .main { background-color: #000000; color: white; }
    .stMetric { background-color: #111; border-radius: 15px; padding: 15px; border: 1px solid #333; }
    .panel-box { background: #111; padding: 20px; border-radius: 15px; border-top: 5px solid #00ff41; margin-bottom: 15px; }
    .event-card { background: #1a1a1a; padding: 10px; border-radius: 8px; border-left: 4px solid #ff00ff; margin-bottom: 8px; font-size: 14px; }
    .label-mini { color: #555; font-size: 11px; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

agora = obter_hora_rio()
h = agora.hour

st.markdown("<h1 style='text-align: center; color: white;'>📡 CENTRAL DE COMANDO RJ</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #666;'>Sincronizado: {agora.strftime('%H:%M')} | Rio de Janeiro</p>", unsafe_allow_html=True)

# --- SEÇÃO 1: FLUXO DETALHADO POR LOCAL ---
st.subheader("✈️ Monitor de Aeroportos & Rodoviária")
col_gig, col_sdu, col_rod = st.columns(3)

# Lógica de Fluxo por Aeroporto e Rodoviária (Estimativa baseada em Malha Real)
def calcular_detalhes(hora):
    # GIG: Pico internacional e conexões longas
    v_gig = 6 if (7 <= hora <= 11 or 19 <= hora <= 23) else 2
    # SDU: Ponte aérea constante
    v_sdu = 8 if (8 <= hora <= 20) else 2
    # Rodoviária: Picos de manhã e noite
    v_rod = 14 if (5 <= hora <= 9) else 4
    return v_gig, v_sdu, v_rod

gig, sdu, rod = calcular_detalhes(h)

with col_gig:
    st.markdown("<div class='panel-box' style='border-top-color: #0088ff;'>", unsafe_allow_html=True)
    st.metric("✈️ GALEÃO (GIG)", f"{gig} Voos", "Próxima Hora")
    st.markdown("<span class='label-mini'>Foco: Viagens Longas / Alta Tarifa</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_sdu:
    st.markdown("<div class='panel-box' style='border-top-color: #00ff41;'>", unsafe_allow_html=True)
    st.metric("✈️ S. DUMONT (SDU)", f"{sdu} Voos", "Próxima Hora")
    st.markdown("<span class='label-mini'>Foco: Executivo / Dinâmico Rápido</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_rod:
    st.markdown("<div class='panel-box' style='border-top-color: #ffa500;'>", unsafe_allow_html=True)
    st.metric("🚌 RODOVIÁRIA", f"{rod} Ônibus", "Chegando agora")
    st.markdown("<span class='label-mini'>Foco: Desembarque Interestadual</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- SEÇÃO 2: EVENTOS E DEMANDA DE HOJE ---
st.divider()
col_ev, col_hot = st.columns([2, 1])

with col_ev:
    st.subheader("🎭 Eventos de Hoje (Principais)")
    # Simulando integração de agenda de eventos
    eventos = [
        {"nome": "Shows na Lapa / Circo Voador", "local": "Centro", "hora": "A partir das 20h"},
        {"nome": "Jogos no Maracanã / Engenhão", "local": "Z. Norte", "hora": "Conferir Tabela"},
        {"nome": "Eventos Corporativos - Riocentro", "local": "Barra", "hora": "Dia todo"},
        {"nome": "Feiras na Praça XV / Centro", "local": "Centro", "hora": "Manhã/Tarde"}
    ]
    for ev in eventos:
        st.markdown(f"""
            <div class="event-card">
                <strong>{ev['nome']}</strong><br>
                <span style="color: #888;">📍 {ev['local']} | ⏰ {ev['hora']}</span>
            </div>
        """, unsafe_allow_html=True)

with col_hot:
    st.subheader("🏨 Check-out")
    if 10 <= h <= 13:
        st.warning("🔥 **ALTA DEMANDA** nos Hotéis de Copacabana e Barra agora!")
        st.markdown("- Hilton (Copa/Barra)\n- Windsor (Orla)\n- Fairmont\n- Hyatt")
    else:
        st.info("🕒 Fluxo normal de hotéis no momento.")

# --- SEÇÃO 3: ESTRATÉGIA ---
st.divider()
st.subheader("🎯 Posicionamento Estratégico")
if 5 <= h <= 9:
    st.success("📍 **ZONA DE FOCO:** RODOVIÁRIA NOVO RIO. Ondas de desembarque massivo de SP e MG.")
elif 16 <= h <= 19:
    st.warning("📍 **ZONA DE FOCO:** CENTRO / SDU. Saída de escritórios e fluxo de Ponte Aérea.")
else:
    st.info("📍 **ZONA DE FOCO:** AEROPORTOS. Monitore o painel de pousos internacionais no GIG.")

# BOTÕES DE APOIO
st.write("")
c1, c2, c3 = st.columns(3)
with c1: st.link_button("Painel GIG Real", "https://www.riogaleao.com/passageiros/voos/painel-de-voos")
with c2: st.link_button("Painel SDU Real", "https://www.infraero.gov.br/voos/index.aspx")
with c3: st.link_button("Agenda Rio Completa", "https://visit.rio/eventos/")
