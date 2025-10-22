from fastapi import APIRouter
from models import PlayerRegistration
from game_state import game_state, INITIAL_HEALTH, MAX_PLAYERS, STANDARD_LIVES, STANDARD_BLASTER

# Setup APIRouter to main
router = APIRouter()
# -----------------------
# API Endpoints
# -----------------------

# Function to assign players to their respective team, using PlayerRegistration obj
@router.post("/register")
def register_player(reg: PlayerRegistration):
    # Check if the match has started
    if game_state["started"]:
        return {"error": "Cannot register during ongoing match"}
    
    if len(game_state["players"]) >= MAX_PLAYERS :
        return {"error": "Maximum players reached, please remove a player"}
    
    # Check if the player id already exists
    if reg.player_id in game_state["players"]:
        return {"error": "Player ID already registered"}
    
    # Add the player to the list of players in the game_state
    game_state["players"][reg.player_id] = {
        "name": reg.player_name or f"Player {reg.player_id}",
        "team": reg.team,
        "health": INITIAL_HEALTH,
        "lives": STANDARD_LIVES,
        "blaster_type": STANDARD_BLASTER,
        "is_alive": True
    }
    # Add the player to the team specified
    game_state["teams"][reg.team].append(reg.player_id)
    
    # Return the details of the game_state and player after registration
    return{
        "message": f"Player {reg.player_id} added to Team {reg.team}",
        "player": game_state["players"][reg.player_id],
        "team_sizes": {team: len(players) for team, players in game_state["teams"].items()}
    }
    
    # TODO: ADD A REMOVE PLAYER ENDPOINT
    
    # TODO: ADD AN EDIT PLAYER ENDPOINT (FUTURE)