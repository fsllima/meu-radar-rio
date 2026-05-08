import streamlit as st
import datetime
import pytz

# Configuração Master do Layout
st.set_page_config(page_title="RADAR REAL TIME RJ", page_icon="📈", layout="wide")

def obter_hora_rio():
    fuso_rio = pytz.timezone('America/Sao_Paulo')
    return datetime.datetime.now(fuso_rio)

# CSS HUD - DESIGN DE ALTA PERFORMANCE
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    .stMetric { background-color: #111; border: 1px solid #333; padding: 20px; border-radius: 20px; }
    .card-real {
        background: linear-gradient(145deg, #111, #050505);
        padding: 25px; border-radius: 15px; border-left: 10px solid #00ff41; margin: 15px 0;
    }
    .hotel-rank { color: #00ff41; font-weight: bold; font-size: 18px; }
    .label-meta { color: #555; font-size: 12px; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

agora = obter_hora_rio()
h = agora.hour

st.markdown("<h1 style='text-align: center;'>⚡ SISTEMA <span style='color: #00ff41;'>REAL TIME</span></h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #444;'>Sincronizado: {agora.strftime('%H:%M')}</p>", unsafe_allow_html=True)

# --- 1. VOLUME REAL PREVISTO (PRÓXIMOS 60 MINUTOS) ---
st.subheader("📊 Fluxo de Chegadas (Ondas)")
col1, col2 = st.columns(2)

# Lógica de contagem baseada na malha real do Rio
def calcular_ondas(hora):
    # Voos (SDU + GIG)
    if 7 <= hora <= 11 or 18 <= hora <= 22:
        v = 12 # PICO: Média de 12 aterrissagens/hora
    elif 12 <= hora <= 17:
        v = 7  # MÉDIO
    else:
        v = 3  # BAIXO
        
    # Ônibus (Rodoviária)
    if 5 <= hora <= 9:
        o = 18 # PICO: Ondas de chegada interestaduais
    elif 17 <= hora <= 20:
        o = 8  # MÉDIO
    else:
        o = 4  # BAIXO
    return v, o

voos, onibus = calcular_ondas(h)

with col1:
    st.metric("✈️ VOOS / HORA", f"{voos} Aviões", "Descendo agora", delta_color="normal")
with col2:
    st.metric("🚌 ÔNIBUS / HORA", f"{onibus} Ônibus", "Chegando na Novo Rio", delta_color="normal")

st.divider()

# --- 2. RANKING DE CHECK-OUT (HOTÉIS TUBARÕES) ---
st.subheader("🏨 Inteligência de Hotéis (Checkout por Volume)")

if 10 <= h <= 13:
    st.markdown(f"""
        <div class="card-real" style="border-left-color: #ffff00;">
            <h3 style="color: #ffff00; margin: 0;">🔥 ALERTA: JANELA DE CHECK-OUT ATIVA</h3>
            <p style="color: #888;">Hotéis com maior número de quartos liberando passageiros:</p>
            <span class="hotel-rank">1. Hilton Copacabana</span> <span class="label-meta">(545 qtos)</span><br>
            <span class="hotel-rank">2. Sheraton Grand</span> <span class="label-meta">(538 qtos)</span><br>
            <span class="hotel-rank">3. Windsor Oceânico</span> <span class="label-meta">(453 qtos)</span><br>
            <span class="hotel-rank">4. Grand Hyatt Barra</span> <span class="label-meta">(436 qtos)</span>
        </div>
    """, unsafe_allow_html=True)
else:
    st.info(f"🕒 Horário focado em **Deslocamento Urbano**. Checkout intenso entre 10:30 e 13:30.")

# --- 3. ESTRATÉGIA DE POSICIONAMENTO ---
st.subheader("🎯 Onde estar agora?")
if 5 <= h <= 9:
    st.success("📍 **RODOVIÁRIA:** Prioridade máxima. 18 ônibus previstos na próxima hora.")
elif 16 <= h <= 19:
    st.warning("📍 **SDU / CENTRO:** Saída de escritórios e Ponte Aérea SP-RJ.")
elif h >= 21 or h <= 2:
    st.error("📍 **GALEÃO / LAPA:** Pousos internacionais e saída de lazer.")
else:
    st.info("📍 **ZONA SUL / BARRA:** Monitorar chamadas curtas e hotéis.")

st.divider()

# --- 4. VERIFICAÇÃO EM TEMPO REAL ---
st.markdown("<p style='text-align: center; color: #333;'>PAINÉIS OFICIAIS AO VIVO</p>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.link_button("✈️ GIG", "https://www.riogaleao.com/passageiros/voos/painel-de-voos")
with c2: st.link_button("✈️ SDU", "https://www.infraero.gov.br/voos/index.aspx")
with c3: st.link_button("📅 EVENTOS", "https://visit.rio/eventos/")

st.caption("Radar Real v5.0 - Dados baseados em malha aérea e capacidade hoteleira.")
