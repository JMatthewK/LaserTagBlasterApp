from fastapi import APIRouter
from game_state import *

# Setup APIRouter to main
router = APIRouter()

# -----------------------
# API Endpoints
# -----------------------

# Function to start the match
@router.post("/match/start")
def start_match():
    # Reset match
    reset_game
    # pid = player_id, 1...8
    for pid in range(1, MAX_PLAYERS + 1):
        game_state["players"]