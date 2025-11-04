import streamlit as st

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

# --- Styles ---
st.markdown(
"""
<style>
body, .stApp {
    background-color: black;
    color: white;
}
div.stButton > button {
    background-color: #facc31;
    color: white;
    font-weight: bold;
    border-radius: 5px;
    height: 3em;
    width: 200px;
}
.karte {
    background-color: #1a1a1a;
    color: white;
    p
