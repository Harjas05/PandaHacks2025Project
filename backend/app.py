import streamlit as st
import os 
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# load apikey safely from.env file
load_dotenv()
API_KEY = os.getenv("HF_TOKEN")
system_prompt = "You are a helpful, empathetic healthcare assistant. You DO NOT diagnose or presribe. Instead, you explain possible causes based on symptoms, suggest when to see a doctor, and give general advice."



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

response = completion.choices[0].message



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