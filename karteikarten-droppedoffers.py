import streamlit as st
import random

# --- CSS Styling ---
st.markdown("""
<style>
body {
    background-color: #000000;  /* Seitenhintergrund */
    font-family: 'Helvetica', sans-serif;
}

/* Titel der Seite */
.custom-title {
    font-size: 32px;
    color: #42c41d;
    font-weight: bold;
    margin-bottom: 20px;
    text-align: center;
}

/* Frage */
.custom-subtitle {
    font-size: 24px;
    color: #ffffff;
    margin-bottom: 15px;
}

/* Antwort */
.custom-answer {
    font-size: 20px;
    color: #f0f0f0;
    margin-bottom: 20px;
}

/* Buttons */
.stButton>button {
    background-color: #facc31;
    color: white;
    font-family: 'Helvetica';
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    padding: 0.5em 1.5em;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    transition: all 0.2s ease;
    margin-top: 10px;
}
.stButton>button:hover {
    background-color: #c9a326;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# --- Karteikarten ---
karten = [
    {"frage": "Quali: Der Kandidat sagt, er will wechseln, weil es seinem aktuellen Arbeitgeber wirtschaftlich schlecht geht. Was gibt es zu beachten?", 
     "antwort": "Nach einem möglichen Abfindungsprogramm / Freiwilligenprogramm fragen"},
    {"frage": "Quali: Der Kandidat sagt, er will wechseln, weil ihm die Herausforderung fehlt und er sich weiterentwickeln will (bspw. zum Senior Entwickler, Softwarearchitekt o.ä.)", 
     "antwort": "Hat er sich intern beworben? Gibt es intern andere Teams / Abteilungen / Produktsparten, die ihn reizen würden? Was könnte sein Arbeitgeber ihm noch anbieten, was ihn reizen würde? (Wichtig: tief nachbohren, Wünsch-Dir-Was-Szenar
