import streamlit as st
import random

# --- Karteikarten (unverändert) ---
karten = [
    {"frage": "Quali: Der Kandidat sagt, er will wechseln, weil es seinem aktuellen Arbeitgeber wirtschaftlich schlecht geht. Was gibt es zu beachten?",
     "antwort": "Nach einem möglichen Abfindungsprogramm / Freiwilligenprogramm fragen"},
    {"frage": "Quali: Der Kandidat sagt, er will wechseln, weil ihm die Herausforderung fehlt und er sich weiterentwickeln will (z.B. zum Senior Entwickler, Softwarearchitekt o.ä.)",
     "antwort": "Hat er sich intern beworben? Gibt es intern andere Teams/Abteilungen/Produktsparten, die ihn reizen würden? Was könnte sein Arbeitgeber ihm noch anbieten (nicht finanziell)?"}, 
    {"frage": "Wie lässt sich eine mögliche Abfindung grob berechnen?",
     "antwort": "Betriebsjahre * Monatsgehalt (Faktor 0,5–1,5)"},
    {"frage": "Kandidat hat andere Prozesse (nicht über uns) und lässt sich nach dem Interview nicht festnageln. Was tun?",
     "antwort": "Kandidat: Fear of Loss, andere Kandidaten on hold // Kunde: transparent sein, dass der Kandidat wenig committed ist, idealerweise andere Profile einsellen // Präventiv: in der Quali Exclusivity holen"},
    {"frage": "Der Kandidat hat in der Quali gesagt, sein Traumjob ist in der Medizintechnik. Er hatte nun ein Final bei deinem Kunden aus einer anderen Branche. Zudem hat er noch andere Prozesse (nicht über uns) in der Medizintechnik, die noch ganz am Anfang sind. Der Kandidat sagt nach dem Final mit deinem Kunden, er fand das Gespräch gut, scheint aber nicht 100% begeistert. Was tun?",
     "antwort": "Den Kandidaten ehrlich fragen: Wenn er seine anderen Prozesse nicht hätte, würde er es dann machen wollen? // Herausfinden, ob es nur ein Plan B oder Backup ist"},
    {"frage": "Der Kunde will das Angebot unbedingt selbst an den Kandidaten schicken oder es ist aus Datenschutzgründen o.ä. nicht möglich, dies über uns zu machen. Was tun?",
     "antwort": "Den Kunden überzeugen, das Offer zumindest erst nach Absprache mit uns zu versenden. // Zudem erfragen: Gibt es etwas im Vertrag, was Erklärungsbedarf braucht? (Überstundenregelung, Urlaubstage, Jobtitel, Homeoffice)"},
    {"frage": "Welche Infos solltest du bei der Quali unbedingt abfragen?",
     "antwort": "Push & Pull Factors, andere Prozesse, Standort/Umzug/Pendeln/Homeoffice/Familie, Gegenangebote, Exclusivity"},
    {"frage": "Wie gehst du mit Kandidaten um, die mehrere Prozesse parallel laufen haben?",
     "antwort": "Fear of Loss, transparente Kommunikation an den Kunden, andere Kandidaten einsellen, durch Exclusivity vorbeugen"},
    {"frage": "Was sind Argumente dagegen, auf ein Gegenangebot einzugehen?",
     "antwort": "Die eigentlichen Gründe der Unzufriedenheit ändern sich nicht (Push Factors aus der Quali) // Die meisten, die darauf eingehen, sind nach ein paar Monaten wieder offen // Versprechungen in der Hitze des Gefechts, die nicht gehalten werden können // Loyalität wird infrage gestellt, der erste auf der „Abschussliste“ bei finanziellen Probleme // ist nur eine Panikhandlung vom Arbeitgeber, da Nachbesetzung und unbesetzte Stellen sehr teuer"},
    {"frage": "Wann sollte das Thema Counter Offer angesprochen werden?",
     "antwort": "Bereits in der Quali"}
]

# --- Session State für zufällige Reihenfolge ---
if "order" not in st.session_state or "pos" not in st.session_state:
    st.session_state.order = list(range(len(karten)))
    random.shuffle(st.session_state.order)
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
if st.session_state.pos >= len(karten):
    st.session_state.pos = 0
    st.session_state.order = list(range(len(karten)))
    random.shuffle(st.session_state.order)

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

        # Wenn am Ende → neu mischen
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
