import streamlit as st
import json
import random

st.markdown("""
<style>
h1 {font-family: 'Helvetica'; font-size: 24px;}   /* Titelgröße */
h2 {font-family: 'Helvetica'; font-size: 20px;}   /* Untertitel */
h3 {font-family: 'Helvetica'; font-size: 20px;}
p  {font-family: 'Helvetica'; font-size: 16px;}   /* normale Texte */

.stButton>button {
    background-color: #F0EFE8;
    color: FACC31;
    border-radius: 10px;
    padding: 0.5em 1.5em;
    font-weight: bold;
    font-size: 16px;  /* Schriftgröße der Buttons */
}
</style>
""", unsafe_allow_html=True)


# Karteikarten
karten = [
    {"frage": "Quali: Der Kandidat sagt, er will wechseln, weil es seinem aktuellen Arbeitgeber wirtschaftlich schlecht geht. Was gibt es zu beachten?", 
     "antwort": "Nach einem möglichen Abfindungsprogramm / Freiwilligenprogramm fragen"},
    {"frage": "Quali: Der Kandidat sagt, er will wechseln, weil ihm die Herausforderung fehlt und er sich weiterentwickeln will (bspw. zum Senior Entwickler, Softwarearchitekt o.ä.)", 
     "antwort": "Hat er sich intern beworben? Gibt es intern andere Teams / Abteilungen / Produktsparten, die ihn reizen würden? Was könnte sein Arbeitgeber ihm noch anbieten, was ihn reizen würde? (Wichtig: tief nachbohren, Wünsch-Dir-Was-Szenario)"},
    {"frage": "Wie lässt sich eine mögliche Abfindung grob berechnen?", 
     "antwort": "Betriebsjahre × Monatsgehalt (Faktor 0,5–1,5)"}
]

# Zufällige Karte merken
if "index" not in st.session_state:
    st.session_state.index = random.randint(0, len(karten)-1)
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

st.title("Client & Candidate Control – Karteikarten")

karte = karten[st.session_state.index]
st.subheader(karte["frage"])

if not st.session_state.show_answer:
    if st.button("Antwort anzeigen"):
        st.session_state.show_answer = True
        st.rerun()
else:
    st.write(f"**Antwort:** {karte['antwort']}")
    if st.button("Nächste Karte"):
        st.session_state.index = random.randint(0, len(karten)-1)
        st.session_state.show_answer = False
        st.rerun()
