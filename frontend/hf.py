
import streamlit as st
#prompt user for input
# get the input and give it to th backend
# get it from the backend and then display it

st.title("AI Doc Assistant")

name = st.text_input("Hi, What's your name?")

user_input = st.text_area("Describe your symptoms please in detail")

