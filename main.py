# Import Uvicorn & the necessary modules from FastAPI
import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
# Import other necessary packages
import OAI_FINETUNING as oaift
import openai
import os
from dotenv import load_dotenv
import json
# Load the environment variables from the .env file into the application
load_dotenv() 
# Initialize the FastAPI application
app = FastAPI()

fine_tuned_model = "ft:gpt-3.5-turbo-0613:personal:olympics:7yxdkrgY"
oaiChatCom = oaift.oaiChatCompletion(fine_tuned_model)

# Create the POST endpoint with path '/queryOlympics'
@app.post("/queryOlympics")
async def oaiChatbot(promptQuery: str):
    print(promptQuery)
    chatresponse = oaiChatCom.fineTunedChatCompletion(promptQuery)
    result_json = json.dumps(chatresponse)
    print("Output Response String - !")
    return result_json

if __name__ == '__main__':
    app.run(debug=True)