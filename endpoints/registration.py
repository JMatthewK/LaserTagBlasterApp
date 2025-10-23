from fastapi import APIRouter
from fastapi import Query
from typing import Literal
from game_state import game_state, INITIAL_HEALTH, MAX_PLAYERS, STANDARD_LIVES, STANDARD_BLASTER

# Setup APIRouter to main
router = APIRouter()
# -----------------------
# API Endpoints
# -----------------------

# Function to assign players to their respective team, using PlayerRegistration obj
@router.post("/register_player")
def register_player(
    player_id: int = Query(..., description="Unique ID of the player"),
    player_name: str | None = Query(None, description="Optional player name"),
    team: Literal["A","B","C","D","E","F","G","H"] = Query(..., description="Team to assign the player")
):
    # Check if the match has started
    if game_state["started"]:
        return {"error": "Cannot register during ongoing match"}
    
    if len(game_state["players"]) >= MAX_PLAYERS :
        return {"error": "Maximum players reached, please remove a player"}
    
    # Check if the player id already exists
    if player_id in game_state["players"]:
        return {"error": "Player ID already registered"}
    
    # Add the player to the list of players in the game_state
    game_state["players"][player_id] = {
        "name": player_name or f"Player {player_id}",
        "team": team,
        "health": INITIAL_HEALTH,
        "lives": STANDARD_LIVES,
        "blaster_type": STANDARD_BLASTER,
        "is_alive": True
    }
    # Add the player to the team specified
    game_state["teams"][team].append(player_id)
    
    # Return the details of the game_state and player after registration
    return{
        "message": f"Player {player_id} added to Team {team}",
        "player": game_state["players"][player_id],
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