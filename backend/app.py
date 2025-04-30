import os 
from typing import List, Dict 
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
from groq import Groq 
from fastapi.middleware.cors import CORSMiddleware 


load_dotenv() 

GROQ_API_KEY = os.getenv("GROQ_API_KEY") 

if not GROQ_API_KEY : 
    raise ValueError("API key for Groq is missing. Please, set the GROQ_API_KEY in the .env file.")

app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins = "*",
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers= ["*"],
    )


client = Groq(api_key=GROQ_API_KEY) 

class UserInput(BaseModel) : 
    message : str
    role : str = 'user'
    conversation_id : str 


