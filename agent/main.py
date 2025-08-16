from importlib import reload
import sys
from tabnanny import verbose
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import re
from langchain_community.chat_models import ChatLlamaCpp
from langchain_core.prompts import ChatPromptTemplate
from typing import Optional
from typing_extensions import Annotated, TypedDict
from prompts.keywords import SYSPROMPTS
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from typing import List
import json


import os

load_dotenv()  # loads .env file in the current working directory
 # prints foo

from langchain_google_genai import ChatGoogleGenerativeAI




# Create FastAPI app instance
app = FastAPI(title="Message Receiver", description="A simple API to receive and print messages")
localllm = ChatLlamaCpp(
    model_path="models/jan/model.gguf",
    temperature=0.0,
    top_p=0.8,
    top_k=20,
    max_tokens=8192,
    n_ctx=40960,
    verbose=False
    )

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)
# Define the message model
class Message(BaseModel):
    content: str

# Define your desired data structure.
class Keywords(BaseModel):
    experience: str = Field(description="years of experience")
    technical: List[str] = Field(...,description="list of technical skills")
    softskill: List[str] = Field(...,description="list of soft skills")
    
# Set up a parser + inject instructions into the prompt template.
parser = JsonOutputParser(pydantic_object=Keywords)

# Store received messages (optional)


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Message Receiver API is running", "endpoints": ["POST /message"]}

@app.post("/extract")
async def receive_message(message: Message):
    """Receive a POST message and print it"""
    index = message.content.find('window.__appData')
# Truncate everything from that point if found
    if index != -1:
        cleaned = message.content[:index]
    else:
        cleaned = message.content
    system_prompt =  PromptTemplate.from_template(
            SYSPROMPTS["keyword"],
    )
    sysprompt = system_prompt.invoke({"format":parser.get_format_instructions()})
    messages =[("system", sysprompt.text),
            ("human", cleaned)]
    print("Processing text", len(cleaned))
    ai =  llm.invoke(messages)
    
    print("generating summary...")
    messages = [("system", SYSPROMPTS["summary"]),
                ("human", ai.content)]
    summary =  llm.invoke(messages)
    print(summary.content)
    
        
        
    

def main():
    """Run the FastAPI server"""
    print("Starting FastAPI server...")
    uvicorn.run("main:app", host="0.0.0.0", port=8848, reload=True)

if __name__ == "__main__":
    print(SYSPROMPTS["summary"])
    main()
    


    
    



