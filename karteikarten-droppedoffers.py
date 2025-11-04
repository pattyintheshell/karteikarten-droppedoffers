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

st.title("Vokabeltrainer / Karteikarten")

karte = karten[st.session_state.index]
st.subheader(f"Frage: {karte['frage']}")

# --- Formular für dynamischen Button ---
with st.form(key="karte_form"):
    # Buttontext dynamisch
    button_label = "Antwort anzeigen" if not st.session_state.show_answer else "Nächste Frage"
    submitted = st.form_submit_button(button_label)

    if submitted:
        if not st.session_state.show_answer:
            st.session_state.show_answer = True
        else:
            st.session_state.index = (st.session_state.index + 1) % len(karten)
            st.session_state.show_answer = False

# Antwort anzeigen
if st.session_state.show_answer:
    st.write(f"**Antwort:** {karte['antwort']}")
