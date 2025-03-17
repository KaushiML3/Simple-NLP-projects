from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse,FileResponse , JSONResponse,HTMLResponse
from pydantic import BaseModel,Field
from typing import List


import uvicorn
import tempfile
import shutil
import os
import warnings


from src.spam import predict_spam
from src.language import predict_language
from src.javaS import js_classification
from src.malicious_url import ULR_Detections

warnings.filterwarnings("ignore")

app=FastAPI(title="Simple NLP project",
    description="FastAPI",
    version="0.115.4")

# Allow all origins (replace * with specific origins if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

@app.get("/")
async def root():
  return {"Fast API":"API is woorking"}


# Suppress warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'  # 0 = all logs, 1 = filter out info, 2 = filter out warnings, 3 = filter out errors
warnings.filterwarnings("ignore")


@app.post("/spam_massage")    
async def spam_detect(message:str):
    try:
        result=predict_spam(message)
        if result is not None:
            return {"status":1,"Message":result}
        else:
            return {"status":0,"Message":"Model prediction error"}
    
    except Exception as e:
        return {"status":0,"Message":e}


@app.post("/language_detection")    
async def language_detect(message:str):
    try:
        result=predict_language(message)
        if result is not None:
            return {"status":1,"Message":result}
        else:
            return {"status":0,"Message":"Model prediction error"}
    
    except Exception as e:
        return {"status":0,"Message":e}
    

@app.post("/JS_detection")    
async def js_detect(JS_text:str):
    try:
        result=js_classification(JS_text)
        if result is not None:
            return {"status":1,"Message":result}
        else:
            return {"status":0,"Message":"Model prediction error"}
    
    except Exception as e:
        return {"status":0,"Message":e}
    
@app.post("/url_verificstion")    
async def url_detect(url:str):
    try:
        result=ULR_Detections(url)
        if result is not None:
            return {"status":1,"Message":result}
        else:
            return {"status":0,"Message":"Model prediction error"}
    
    except Exception as e:
        return {"status":0,"Message":e}

if __name__=="__main__":
    
    uvicorn.run("app:app",host="0.0.0.0", port=8000, reload=True)