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
    margin-bottom: 30px;
    text-align: center;
}

/* Karteikarte Box */
.card {
    background-color: #1c1c1c;   /* dunkle Box */
    border-radius: 15px;
    padding: 20px 25px;
    margin-bottom: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.5);
}

/* Frage innerhalb der Karte */
.card .question {
    font-size: 22px;
    color: #facc31;
    font-weight: bold;
    margin-bottom: 15px;
}

/* Antwort innerhalb der Karte */
.card .answer {
    font-size: 20px;
    color: #ffffff;
    line-height: 1.5;
    margin-top: 10px;
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
     "antwort": "Hat er sich intern beworben? Gibt es intern andere Teams / Abteilungen / Produktsparten, die ihn reizen würden? Was könnte sein Arbeitgeber ihm noch anbieten, was ihn reizen würde? (Wichtig: tief nachbohren, Wünsch-Dir-Was-Szenario)"},
    {"frage": "Wie lässt sich eine mögliche Abfindung grob berechnen?", 
     "antwort": "Betriebsjahre × Monatsgehalt (Faktor 0,5–1,5)"}
]

# --- Session State ---
if "index" not in st.session_state:
    st.session_state.index = random.randint(0, len(karten)-1)
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

# --- Anzeige ---
st.markdown("<div class='custom-title'>Client & Candidate Control – Karteikarten</div>", unsafe_allow_html=True)

karte = karten[st.session_state.index]

# Karteikarte mit Frage
st.markdown(f"""
<div class='card'>
    <div class='question'>{karte['frage']}</div>
    {"<div class='answer'><b>Antwort:</b> " + karte['antwort'] + "</div>" if st.session_state.show_answer else ""}
</div>
""", unsafe_allow_html=True)

# Buttons
if not st.session_state.show_answer:
    if st.button("Antwort anzeigen"):
        st.session_state.show_answer = True
        st.experimental_rerun()
else:
    if st.button("Nächste Karte"):
        st.session_state.index = random.randint(0, len(karten)-1)
        st.session_state.show_answer = False
        st.experimental_rerun()
