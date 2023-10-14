import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

st.set_page_config(page_title="Finn",
                   page_icon=":brain:", layout="wide")


def load_lottie(url: str):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()

# Use local CSS


def local_css(filename: str):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css('style/style.css')

# ---- LOAD ASSETS ----
LOTTIE_CODING = load_lottie(
    "https://lottie.host/9bb823dd-6461-432c-a8b6-f994d655fe6c/xQ2jt5uzdg.json")
FINNVENTIONS_LOGO = Image.open('images/finnventions-logo.png')
GALLEONS = Image.open('images/galleons.png')
WORDLEBOT = Image.open('images/wordlebot.png')
WORDLE_SOLUTIONS = Image.open('images/wordle-solutions.png')
COMPUTER_SCIENCE = Image.open('images/computer-science.png')

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Finn :wave:")
    st.title("A kid from the US")
    st.write("I am really passionate about learning many ways to code things.")
    st.write(
        "[My first webpage](https://the-real-finnventor.github.io/wordle-solutions-website/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("I go around looking for different things to learn. These are mostly python web frameworks currently. I specialize in python though I also do plenty of other things.")
        st.write("[My blog](https://finnventions.com)")
    with right_column:
        st_lottie(LOTTIE_CODING, height=300, key="coding")


# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(FINNVENTIONS_LOGO)
    with text_column:
        st.subheader("Insult")
        st.write("MacOS command line program that speaks insults to your enemies.")
        st.markdown(
            "[Vist github repo](https://github.com/the-real-finnventor/insult)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(GALLEONS)
    with text_column:
        st.subheader("Galleon Conversion Website")
        st.write("A website that converts Harry Potter money into real money.")
        st.markdown(
            "[Vist website](https://the-real-finnventor.github.io/galleon-convertion-website/)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(WORDLEBOT)
    with text_column:
        st.subheader("Wordlebot")
        st.write(
            "A python script that uses logic to solve [the New York Times Wordle game](https://www.nytimes.com/games/wordle/).")
        st.markdown(
            "[Vist github repo](https://github.com/the-real-finnventor/wordle-bot)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(WORDLE_SOLUTIONS)
    with text_column:
        st.subheader("Wordle Solutions Website")
        st.write(
            "A website that shows you the all of the possible answers for [the New York Times Wordle game](https://www.nytimes.com/games/wordle/).")
        st.markdown(
            "[Vist website](https://the-real-finnventor.github.io/wordle-solutions-website/)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(COMPUTER_SCIENCE)
    with text_column:
        st.subheader("Computer Science")
        st.write(
            "A github repo that stores all my computer science projects.")
        st.markdown(
            "[Vist github repo](https://github.com/the-real-finnventor/computer-science)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")
    CONTACT_FORM = """
<form action="https://formsubmit.co/finnventor@everspaugh.com" method="POST">
    <input type=\"text\" name="name\" placeholder=\"Your name\" required>
    <input type=\"email\" name="email\" placeholder=\"Your email\" required>
    <textarea name=\"message\" placeholder=\"Your message\" required></textarea>
    <button type=\"submit\">Send</button>
</form>
"""
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(CONTACT_FORM, unsafe_allow_html=True)
    with right_column:
        st.empty()
