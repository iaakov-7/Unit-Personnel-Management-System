from pydantic import BaseModel
from enum import Enum


class SoldierRank(str,Enum):
    PRIVATE =  "Private" 
    SERGEANT =   "Sergeant"
    CAPTAIN = "Captain"

class Soldier(BaseModel):
    id:int
    name:str
    rank: SoldierRank

class SoldierUpdate(BaseModel):
    name:str | None = None
    rank:SoldierRank | None = None


def find_by_id(soldiers,id):
    for soldier in soldiers:
        if soldier.get("id") == id:
            return soldier
    return None 