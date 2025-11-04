import streamlit as st

# --- Karteikarten ---
karten = [
    {"frage": "Quali: Der Kandidat sagt, er will wechseln, weil es seinem aktuellen Arbeitgeber wirtschaftlich schlecht geht. Was gibt es zu beachten?",
     "antwort": "Nach einem möglichen Abfindungsprogramm / Freiwilligenprogramm fragen"},
    {"frage": "Quali: Der Kandidat sagt, er will wechseln, weil ihm die Herausforderung fehlt und er sich weiterentwickeln will (z.B. zum Senior Entwickler, Softwarearchitekt o.ä.)",
     "antwort": "Hat er sich intern beworben? Gibt es intern andere Teams/Abteilungen/Produktsparten, die ihn reizen würden? Was könnte sein Arbeitgeber ihm noch anbieten?"}, 
    {"frage": "Wie lässt sich eine mögliche Abfindung grob berechnen?",
     "antwort": "Betriebsjahre * Monatsgehalt (Faktor 0,5–1,5)"}
]

# --- Session State ---
if "index" not in st.session_state:
    st.session_state.index = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

# --- CSS Styles für edlen Look + Fade-In ---
css = "<style>" \
      "body, .stApp { background-color: #121212; color: white; }" \
      "div.stButton > button { background-color: #facc31; color: white; font-weight: bold; border-radius:5px; height:3em; width:200px; }" \
      ".frage { background-color:#2b2b2b; color:white; padding:20px; border-radius:10px; margin-bottom:20px; box-shadow:0 8px 20px rgba(0,0,0,0.5); transition: transform 0.2s; }" \
      ".antwort { background-color:#181818; color:white; padding:20px; border-radius:10px; margin-bottom:20px; box-shadow:0 8px 20px rgba(0,0,0,0.5); transition: transform 0.2s, opacity 0.5s; opacity:0; animation: fadein 0.5s forwards; }" \
      ".frage:hover, .antwort:hover { transform: translateY(-5px); }" \
      "@keyframes fadein { from {opacity:0;} to {opacity:1;} }" \
      "</style>"
st.markdown(css, unsafe_allow_html=True)

st.title("Candidate & Client Control")

# --- sichere Karte abrufen ---
index = st.session_state.index % len(karten)
karte = karten[index]

# Frage anzeigen
st.markdown(f"<div class='frage'><b>Frage:</b> {karte['frage']}</div>", unsafe_allow_html=True)

# --- Button-Funktion ---
def next_card():
    if not st.session_state.show_answer:
        st.session_state.show_answer = True
    else:
        st.session_state.index = (st.session_state.index + 1) % len(karten)
        st.session_state.show_answer = False

button_text = "Antwort anzeigen" if not st.session_state.show_answer else "Nächste Frage"
st.button(button_text, on_click=next_card)

# Antwort anzeigen
if st.session_state.show_answer:
    st.markdown(f"<div class='antwort'><b>Antwort:</b> {karte['antwort']}</div>", unsafe_allow_html=True)
