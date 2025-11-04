import streamlit as st

# Session State
if "index" not in st.session_state:
    st.session_state.index = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

karten = [
    {"frage": "Frage 1", "antwort": "Antwort 1"},
    {"frage": "Frage 2", "antwort": "Antwort 2"}
]

# Funktion
def next_card():
    if not st.session_state.show_answer:
        st.session_state.show_answer = True
    else:
        st.session_state.index = (st.session_state.index + 1) % len(karten)
        st.session_state.show_answer = False

# Styles
st.markdown("""
<style>
div.stButton > button {
    background-color: #facc31;
    color: white;
    font-weight: bold;
    border-radius:5px;
    height:3em;
    width:200px;
}
</style>
""", unsafe_allow_html=True)

karte = karten[st.session_state.index]
st.markdown(f"<div style='background-color:#1a1a1a; color:white; padding:20px; border-radius:10px; margin-bottom:20px;'>{karte['frage']}</div>", unsafe_allow_html=True)

button_text = "Antwort anzeigen" if not st.session_state.show_answer else "Nächste Frage"
st.button(button_text, on_click=next_card)

if st.session_state.show_answer:
    st.markdown(f"<div style='background-color:#1a1a1a; color:white; padding:20px; border-radius:10px; margin-top:20px;'>{karte['antwort']}</div>", unsafe_allow_html=True)
