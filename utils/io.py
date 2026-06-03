import json
import os
from fastapi import HTTPException
from logger_config import logger

def load_from_json(path):
    if not os.path.exists(path):
        with open(path,"w",encoding="utf-8") as file:
            json.dump([],file,indent=2)
            return []
    try:    
        with open(path,"r",encoding="utf-8") as file:
            data = json.load(file)
            return data  
    except json.decoder.JSONDecodeError:
        logger.error("File is empty") 
        raise HTTPException(status_code=500,detail="File is empty")     

def save_to_json(data,path):
            with open(path,"w",encoding="utf-8") as file:
                json.dump(data,file,indent=2)


