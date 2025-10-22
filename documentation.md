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