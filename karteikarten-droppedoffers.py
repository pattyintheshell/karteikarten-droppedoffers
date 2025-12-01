import streamlit as st
import random

# --- Karteikarten ---
karten = [
    {"frage": "Quali: Der Kandidat sagt, er will wechseln, weil es seinem aktuellen Arbeitgeber wirtschaftlich schlecht geht. Was gibt es zu beachten?",
     "antwort": "Nach einem möglichen Abfindungsprogramm / Freiwilligenprogramm fragen"},
    {"frage": "Quali: Der Kandidat sagt, er will wechseln, weil ihm die Herausforderung fehlt und er sich weiterentwickeln will (z.B. zum Senior Entwickler, Softwarearchitekt o.ä.)",
     "antwort": "Hat er sich intern beworben? Gibt es intern andere Teams/Abteilungen/Produktsparten, die ihn reizen würden? Was könnte sein Arbeitgeber ihm noch anbieten?"}, 
    {"frage": "Wie lässt sich eine mögliche Abfindung grob berechnen?",
     "antwort": "Betriebsjahre * Monatsgehalt (Faktor 0,5–1,5)"},
    {"frage": "Nach dem 1st oder Final Interview: Der Kandidat hat andere Prozesse (nicht über uns) und lässt sich nicht festnageln. Was tun?",
     "antwort": "Kandidat: Fear of Loss, andere Kandidaten on hold // Kunde: transparent sein, dass der Kandidat wenig committed ist, idealerweise andere Profile einsellen // Präventiv: in der Quali Exclusivity holen"},
    {"frage": "Der Kandidat hat dir in der Quali gesagt, sein Traumjob ist in der Medizintechnik. Er hatte nun ein Final bei deinem Kunden aus der Industriellen Automatisierung. Zudem hat er noch andere Prozesse (nicht über uns) in der Medizintechnik, die zeitlich nicht so weit sind. Der Kandidat sagt nach dem Final mit deinem Kunden, er fand das Gespräch gut, scheint aber nicht 100% richtig begeistert. Wie machst du hier weiter?",
     "antwort": "Den Kandidaten ehrlich fragen: Wenn er seine anderen Prozesse nicht hätte, würde er es dann machen wollen? // Herausfinden, ob es nur ein Plan B / Notfall ist"},
    {"frage": "Der Kunde will das Offer unbedingt selbst verschicken bzw. es ist aus Datenschutzgründen o.ä. nicht möglich, das Offer über uns zu senden. Was tun?",
     "antwort": "Den Kunden überzeugen, das Offer zumindest erst nach Absprache mit uns zu versenden. // Zudem fragen: Gibt es etwas im Vertrag, was Erklärungsbedarf braucht? (Überstundenregelung, Urlaubstage, Jobtitel, Homeoffice)"}
]

# --- Session State für zufällige Reihenfolge ---
if "order" not in st.session_state:
    st.session_state.order = list(range(len(karten)))
    random.shuffle(st.session_state.order)

if "pos" not in st.session_state:
    st.session_state.pos = 0

if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

# --- CSS Styles ---
css = """
<style>
body, .stApp {
    background-color: #121212;
    color: white;
}

div.stButton > button {
    background-color: #facc31;
    color: white;
    font-weight: bold;
    border-radius: 5px;
    height: 3em;
    width: 200px;
    transition: background-color 0.2s;
}

div.stButton > button:hover {
    background-color: #e6b800;
}

.frage {
    background-color: #2b2b2b;
    color: white;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.5);
    transition: transform 0.2s;
}

.antwort {
    background-color: #181818;
    color: white;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.5);
    transition: transform 0.2s, opacity 0.5s;
    opacity: 0;
    animation: fadein 0.5s forwards;
}

.frage:hover, .antwort:hover {
    transform: translateY(-5px);
}

b.label {
    font-size: 1.3em;
    font-weight: 900;
    color: #facc31;
}

@keyframes fadein {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# --- Titel ---
st.title("Candidate & Client Control")

# --- aktuelle Karte holen ---
current_index = st.session_state.order[st.session_state.pos]
karte = karten[current_index]

# --- Frage anzeigen ---
st.markdown(
    f"<div class='frage'><b class='label'>Frage:</b> {karte['frage']}</div>",
    unsafe_allow_html=True
)

# --- Button Logik ---
def next_card():
    if not st.session_state.show_answer:
        st.session_state.show_answer = True
    else:
        st.session_state.show_answer = False
        st.session_state.pos += 1

        # Deck komplett durch → neu mischen
        if st.session_state.pos >= len(karten):
            st.session_state.pos = 0
            st.session_state.order = list(range(len(karten)))
            random.shuffle(st.session_state.order)

button_text = "Antwort anzeigen" if not st.session_state.show_answer else "Nächste Frage"
st.button(button_text, on_click=next_card)

# --- Antwort anzeigen ---
if st.session_state.show_answer:
    st.markdown(
        f"<div class='antwort'><b class='label'>Antwort:</b> {karte['antwort']}</div>",
        unsafe_allow_html=True
    )
