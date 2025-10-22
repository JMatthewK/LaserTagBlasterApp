# ESP32 LaserTag System
**Laser tag system powered by ESP32 microcontrollers, IR sensors and a Python backend with web integration**

## Overview
This projects goal is to build a standalone laser tag system that will use ESP32 microcontrollers in blasters and vests.
Each blaster and vest will communicate over Wi-Fi, detecting hits through IR sensors and syncing it with a web app to show the live game state.
The design is built around workin goffline on a local network, possibly with a Raspberry Pi hosting the backend and MQTT broker.
A hub, blasters and vest will allow anyone to play lasertag at home.

## Project Goals
- Open-source DIY friendly laser tag platform using inexpensive hardware.
- Fast and lightweight game logic.
- Python FastAPI backend to collect and display live game data.
- To provide a modern web UI for the scoreboard, match settings and analytics after each game.
- After a prototype is built, would consider expanding it into a bigger idea.

