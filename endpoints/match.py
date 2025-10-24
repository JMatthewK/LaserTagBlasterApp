from fastapi import APIRouter
from game_state import game_state, reset_game, INITIAL_HEALTH, STANDARD_LIVES, STANDARD_BLASTER
from datetime import datetime

# Setup APIRouter to main
router = APIRouter()

# -----------------------
# API Endpoints
# -----------------------

# Function to start the match
@router.post("/match/start")
def start_match():
    """
    Starts the match if registration has been done successfully
    """
    # Check if match has started already
    if game_state["started"]:
        return {"error": "Match already started.",
                "Match started: ": game_state["started"],}
    
    # Make sure enough players exist by making sure there's at least 1 player in at least 2 teams
    active_teams = sum(1 for players in game_state["teams"].values() if len(players) > 0)

    if active_teams < 2:
        return {"error": "Not enough teams with players to start the match.",
                "Match started: ": game_state["started"],}
    
    # Set each players health and lives to it's initials
    for player_id, player in game_state["players"].items():
        player["health"] = INITIAL_HEALTH
        player["lives"] = STANDARD_LIVES
        player["points"] = 0
        player["is_alive"] = True
        player["blaster_type"] = STANDARD_BLASTER
    
    game_state["started"] = True
    # Timer system for later
    game_state["start_time"] = datetime.utcnow()
    game_state["end_time"] = None
    
    # Log team sizes
    team_sizes = {team: len(players) for team, players in game_state["teams"].items()}

    # Return the team sizes and list of players
    return {
        "message": "Match started successfully.",
        "Match started: ": game_state["started"],
        "team_sizes": team_sizes,
        "players": [player["name"] for player in game_state["players"].values()]

    }

# Function to reset the match (remove players and reset everything)
@router.post("/match/reset")
def reset_match():
    """
    Resets all information that was added during player registration
    """
    # Reset the match using the reset_game function from the game_state
    reset_game()
    return{"message": f"Match reset.",
           "team_sizes": {team: len(players) for team, players in game_state["teams"].items()}
    }
    
# Function to end the match
@router.post("/match/end")
def end_match():
    """
    Ends the match but doesn't reset the match
    """
    
    # Check if match is in progress
    if game_state["started"] == False:
        return {"error": "Match not started.",
                "Match started: ": game_state["started"],}
        
    # Set the game_state to not started
    
    game_state["started"] == False
    
    # Return the team sizes and list of players
    return {
        "message": "Match ended successfully.",
        "Match started: ": game_state["started"],
    }