import streamlit as st
import random

# --- Karteikarten ---
karten = [
    {"frage": "Quali: Der Kandidat sagt, er will wechseln, weil es seinem aktuellen Arbeitgeber wirtschaftlich schlecht geht. Was gibt es zu beachten?",
     "antwort": "Nach einem möglichen Abfindungsprogramm / Freiwilligenprogramm fragen"},
    {"frage": "Quali: Der Kandidat sagt, er will wechseln, weil ihm die Herausforderung fehlt und er sich weiterentwickeln will (z.B. zum Senior Entwickler, Softwarearchitekt o.ä.)",
     "antwort": "Hat er sich intern beworben? Gibt es intern andere Teams/Abteilungen/Produktsparten, die ihn reizen würden? Was könnte sein Arbeitgeber ihm noch anbieten?"}, 
    {"frage": "Wie lässt sich eine mögliche Abfindung grob berechnen?",
     "antwort": "Betriebsjahre × Monatsgehalt (Faktor 0,5–1,5)"}
]

# --- Session State ---
if "index" not in st.session_state:
    st.session_state.index = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

# --- Style ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;
    }
    .karte {
        background-color: #1a1a1a;
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .button-style button {
        background-color: #facc31;
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Candidate & Client Control")

karte = karten[st.session_state.index]
st.markdown(f"<div class='karte'><b>Frage:</b> {karte['frage']}</div>", unsafe_allow_html=True)

# --- Buttonlogik ---
def button_action():
    if not st.session_state.show_answer:
        st.session_state.show_answer = True
    else:
        st.session_state.index = (st.session_state.index + 1) % len(karten)
        st.session_state.show_answer = False

button_text = "Antwort anzeigen" if not st.session_state.show_answer else "Nächste Frage"
st.markdown(f"<div class='button-style'>{st.button(button_text, on_click=button_action)}</div>", unsafe_allow_html=True)

# Antwort anzeigen
if st.session_state.show_answer:
    st.markdown(f"<div class='karte'><b>Antwort:</b> {karte['antwort']}</div>", unsafe_allow_html=True)
