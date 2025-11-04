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

# --- CSS Styles für edlen Look ---
css = '''
<style>
/* Hintergrund der App */
body, .stApp {
    background-color: #121212;  /* dunkles Anthrazit */
    color: white;
}

/* Button-Stil */
div.stButton > button {
    background-color: #facc31;
    color: white;
    font-weight: bold;
    border-radius: 5px;
    height: 3em;
    width: 200px;
}

/* Karteikarten-Stil */
.karte {
    background-color: #1f1f1f;  /* helleres Grau für die Karten */
    color: white;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);  /* leichter Schatten für 3D-Effekt */
    transition: transform 0.2s;  /* sanfte Hover-Animation */
}

/* Hover-Effekt für die Karten */
.karte:hover {
