from fastapi import APIRouter
from backend.app.models import PlayerRegistration
from backend.app.game_state import game_state, INITIAL_HEALTH, MAX_PLAYERS, STANDARD_LIVES, STANDARD_BLASTER

# Setup APIRouter to main
router = APIRouter()
# -----------------------
# API Endpoints
# -----------------------

# Function to assign players to their respective team, using PlayerRegistration obj
@router.post("/register_player")
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
        "points": 0,
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
@router.post("/remove_player")
def remove_player(pid: int):
    """
    Remove a player from the game using their Player ID

    Args:
        pid (int): The ID of the player to be removed
    """
    # Check if the match has started
    if game_state["started"]:
        return {"error": "Cannot register during ongoing match"}
    
    # Make sure player id exists in the list of players
    if pid not in game_state["players"]:
        return {"error": f"Player with ID {pid} not found."}
    
    # Retrieve team before removing the player
    team_name = game_state["players"][pid]["team"]

    # Remove player from team list if present
    if pid in game_state["teams"][team_name]:
            game_state["teams"][team_name].remove(pid)
    
    removed_player = game_state["players"].pop(pid)


    return{"message": f"Player {pid} removed successfully.",
           "team_sizes": {team: len(players) for team, players in game_state["teams"].items()}
    }


# TODO: ADD AN EDIT PLAYER ENDPOINT (FUTURE)