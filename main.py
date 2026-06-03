from fastapi import FastAPI,status,HTTPException
from utils.io import save_to_json,load_from_json
from utils.helper import find_by_id,Soldier
from logger_config import logger


app = FastAPI()
SOLDIERS_FILE = "soldiers.json"

@app.get('/soldiers', status_code=200)
def get_all_soldiers():
    logger.info("Incoming request: Attempting to fetch all soldiers")
    soldiers = load_from_json(SOLDIERS_FILE)
    if len(soldiers) == 0:
        logger.warning("There are no soldiers in list")
    logger.info(f"Read {len(soldiers)} soldiers from list")    
    return soldiers    

@app.get("/soldiers/{soldier_id}",status_code=200)
def get_soldier_by_id(soldier_id:int):
    logger.info(f"Incoming request: Attempting to fetch soldier with id {soldier_id}")
    soldiers = load_from_json(SOLDIERS_FILE)
    soldier = find_by_id(soldiers,soldier_id)
    if not soldier:
        logger.warning(f"Soldier with id {soldier_id} not found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Soldier with id {soldier_id} not found ")
    logger.info(f"Read soldier with id {soldier_id} ") 
    return soldier
       
@app.post("/soldiers",status_code=201)
def create_soldier(new_soldier:Soldier):
    logger.info(f"Incoming request: Attempting to create a new soldier")
    soldiers = load_from_json(SOLDIERS_FILE)
    soldier = new_soldier.model_dump()
    if find_by_id(soldiers,soldier.get("id")):
        logger.error(f"Soldier with id {soldier.get('id')} is already exists")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Soldier with id {soldier.get('id')} is already exists") 
    soldiers.append(soldier)
    save_to_json(soldiers,SOLDIERS_FILE)
    logger.info(f"Soldier with id {soldier.get('id')} created successfully")
    return {"Message":f"soldier with id {soldier.get('id')} created successfully"}

@app.put("/soldiers/{soldier_id}")
def update_soldier(soldier_id:int,updated_soldier:Soldier):
    logger.info(f"Incoming request: Attempting to update soldier with id {soldier_id}")
    soldiers = load_from_json(SOLDIERS_FILE)
    soldier = find_by_id(soldiers,soldier_id)
    if not soldier:
        logger.warning(f"Soldier with id {soldier_id} not found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Soldier with id {soldier_id} not found ")
    soldiers.remove(soldier)
    updated_soldier = updated_soldier.model_dump()
    updated_soldier["id"] = soldier_id
    soldiers.append(updated_soldier)
    save_to_json(soldiers,SOLDIERS_FILE)
    logger.info(f"Soldier with id {soldier_id} updated successfully")
    return {"Message":f"soldier with id {soldier_id} updated successfully"} 

@app.delete("/soldiers/{soldier_id}")
def delete_soldier(soldier_id:int):
    logger.info(f"Incoming request: Attempting to delete soldier with id {soldier_id}")
    soldiers = load_from_json(SOLDIERS_FILE)
    soldier = find_by_id(soldiers,soldier_id)
    if not soldier:
        logger.warning(f"Soldier with id {soldier_id} not found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Soldier with id {soldier_id} not found ")
    soldiers.remove(soldier)
    save_to_json(soldiers,SOLDIERS_FILE)
    logger.info(f"Soldier with id {soldier_id} deleted successfully")
    return {"Message":f"soldier with id {soldier_id} deleted successfully"}    
