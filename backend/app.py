import streamlit as st
import os 
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
# from backend import hf

# load apikey safely from.env file
load_dotenv()
API_KEY = os.getenv("HF_TOKEN")
system_prompt = "You are a helpful, empathetic healthcare assistant. You DO NOT diagnose or presribe. Instead, you explain possible causes based on symptoms, suggest when to see a doctor, and give general advice."

st.title("AI Doc Assistant")

name = st.text_input("Hi, What's your name?")

user_input = st.text_area(f"Hi {name}!! Describe your symptoms please in detail")


client = InferenceClient(
    provider="cerebras",
    api_key=API_KEY,
)

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct",
    messages=[
        {
            "role": "system",
            "content": f"{system_prompt}"
        },
        {
            "role": "user",
            "content": f"{user_input}"
        }
    ],
)

# response = completion.choices[0].message

if st.button("Enter") and user_input :
    response = completion.choices[0].message.content
    st.text_area(label ="",value=response, height =100) # need to find a way to make it not scroll

    #add in continuous chat feature



#get the user input from the front-end 
#store it and then pass it off to the llm
# sanitize?
# Construct prompt for LLM
# Call Hugging Face model using Inference API
# Return structured response to frontend





#prompt the user for symptoms
# repeat until user ends chat
# store symptoms
# send to prompt
# send llm 
# give the answer that the llm gave to the user 
# one chat per page