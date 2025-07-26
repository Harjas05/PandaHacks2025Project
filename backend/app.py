import streamlit as st
import os 
from dotenv import load_dotenv

# load apikey safely from.env file
load_dotenv()
API_KEY = os.getenv("HF_TOKEN")

#get the user input from the front-end 
#store it and then pass it off to the llm
# sanitize?
#Construct prompt for LLM
# Call Hugging Face model using Inference API
# Return structured response to frontend





#prompt the user for symptoms
# repeat until user ends chat
# store symptoms
# send to prompt
# send llm 
# give the answer that the llm gave to the user 
# one chat per page