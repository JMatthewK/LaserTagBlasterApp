from pydantic import BaseModel 
from typing import Literal
# -----------------------
# Data Models
# -----------------------

# Hit object for every hit that happens for processing
class HitEvent(BaseModel):
    blasterId: int
    targetId: int
    timestamp: str
    hitLocation: str
    
# Player registration class 
class PlayerRegistration(BaseModel):
    player_id: int
    player_name: str = None # optional none name 
    team: Literal["A","B","C","D","E","F","G","H"]