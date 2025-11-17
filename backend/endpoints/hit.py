from fastapi import APIRouter
from fastapi import Body
from backend.app.game_state import game_state, INITIAL_HEALTH, STANDARD_BLASTER

# Setup APIRouter to main
router = APIRouter()

# -----------------------
# API Endpoints
# -----------------------

# Hit endpoint
@router.post("/hit")
def hit_player(
    target_id: int = Body(..., embed=True),
    shooter_id: int = Body(..., embed=True),
    damage: int = Body(10, embed=True),
    hit_zone: str = Body("CHEST", embed=True)
):
    if not game_state["started"]:
        return {"error": "Match has not started"}
    
    if target_id not in game_state["players"]:
        return {"error": "Target player does not exist"}
    
    if shooter_id not in game_state["players"]:
        return {"error": "Shooting player does not exist"}
    
    
    shooter = game_state["players"][shooter_id]
    target = game_state["players"][target_id]
    
    if not target["is_alive"]:
        return {"error": "Target already eliminated."}
    
    # Make sure players are not on the same team
    if shooter["team"] == target["team"]:
        return {"error": "Shooter and Target on same team"}
    
    # TODO: Check where the opponent was hit, determine damage based on blaster
    
    # Subtract the target health based on the damage
    target["health"] -= damage
    
    
    if target["health"] <= 0:
        if target["lives"] is not None:
            target["lives"] -= 1
            
            # Only used when game includes lives, default is a infinite point based game
            if target["lives"] > 0:
                target["health"] = INITIAL_HEALTH
                target["blaster_type"] = STANDARD_BLASTER
            else:
                target["is_alive"] = False
        else:
            shooter["points"] += 1
            target["health"] = INITIAL_HEALTH
            target["blaster_type"] = STANDARD_BLASTER
    
    return {
        "message": f"Shooter {shooter_id} hit Target {target_id} in zone {hit_zone} for {damage} damage",
        "target status:": {
            "health": target["health"],
            "lives": target["lives"],
            "is_alive": target["is_alive"]
        },
        "shooter status:": {
            "shooter points": shooter["points"]
            }
    }
        
