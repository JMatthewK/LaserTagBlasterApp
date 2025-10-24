Here was my process of making this app

Learning FastApi
downloaded fastapi and uvicorn
$ pip install fastapi uvicorn

fastapi is the framework and uvicorn is the web server running

2. Made a basic main file and then used uvicorn main:app --reload to run it

127.0.0.1:8000 is the server used
http://127.0.0.1:8000/docs is the interactive UI

a "route decorator" is @app.get("/") which tells the app that when someone visits the URL to run the function

FastAPI routes (endpoints)
GET - Fetches data 
POST - Sends new data
PUT - Update existing data
DELETE - Remove data

3. @app.post("/hit")
- When someone sends a POST request to /hit, FastAPI will parse the incoming JSON into a Hit object
- Validates it
- Returns the JSON

This is how the ESP32 will send hit data

*I decided that before anything else I should solidify my backend to have the endpoints i need for the basics of the lasertag game*

I learnt that constants in python are normally CAPITALIZED

from typing import Literal
Literal["A", "B"] makes it so that only A and B can be submitted

4. I DECIDED I should probably structure the app
main.py # Starts the app
models.py # holds the pydantic models
game_state.py # Controls the game state dictionaries, keeps helper functions and constants
endpoints # Folder with all endpoints
- match.py #match endpoints
- hit.py # hit endpoints
- register.py # registration endpoints etc

5. I worked on adding registration, so adding and removing players. I think the next step is to setup a game, and then have a UI I can read in the terminal
I'll work on starting the match and being able to register hits from one player to another. Once that is set, I can start working on the code from the ESP32.

6. Getting ready for the flow of the game

Essentially there are 3 stages

    1. Game setup
        - Adding and removing players
        - Assigning teams
        - Preparing game state
        - Then using /match/start
    2. Game in progress
        - Players shoot and get hit
        - Update the health and lives per hit
        - Track who is hitting who and record stats
        - /hit endpoint will be used here
            - I assume the logic to determine when to call the hit endpoint will be determined when I make the logic for the ESP32
    3. Post-match
        - Determine who won, and determine the stats
        - Stop all hits from being registered
        - GIVE THE OPTION TO EITHER
            - Reset the state of the match
            - Replay with same players
                - Change teams
                - Same teams


**Half way through doing all of this I decided it might be a good idea to instead use cameras and openCV to detect instead of IR, I think this could be a cool breakthrough for home lasertag systems**

I also think a good idea is to have a OLED screen on each blaster to see your health and lives and update where you got hit etc etc

**I realized that doing everything with a camera would create the problem of not knowing who got hit because it may mistake players. SO a combo of IR and CV could be baller**


7. I am finally at the point of the API where I can register/remove players start a game, register hits and then end a game where it will reset.