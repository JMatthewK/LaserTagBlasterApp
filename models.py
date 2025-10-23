from pydantic import BaseModel 
# -----------------------
# Data Models
# -----------------------

# Hit object for every hit that happens for processing
class HitEvent(BaseModel):
    blasterId: int
    targetId: int
    timestamp: str
    hitLocation: str