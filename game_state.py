# -----------------------
# Game State
# -----------------------
MAX_PLAYERS = 8
INITIAL_HEALTH = 100
STANDARD_LIVES = 3
STANDARD_BLASTER = "pistol"

game_state = {
    "started": False,
    # A and B are the primary teams with all other teams being there for custome gamemodes
    "teams": {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
        "H": []
    },
    # Players should be in the format
    # player_id: {"name" "team", "health", "lives", "blaster_type", "is_alive"}
    "players": {
        
    }
    
}

# -----------------------
# Functions
# -----------------------
def reset_game():
    """Resets all the players and states"""
    game_state["started"] = False
    game_state["players"] = {}
    game_state["teams"] = {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
        "H": []
    },