# Pong Game 🏓

Simulates the classic pong style game. Match the paddle to the ball!

## Running the game

Install Python from the official Python website.
Clone https://github.com/aidanwalsh13/Pong-game.git

In the pong directory run the game with the following options:

#### Option 1: Using uv (recommended)

uv run main.py

#### Option 2: Using python

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install .
python main.py

### Features
- Classic Pong mechanics
- 2 Players required
- First to 5, wins
- As the rally lasts the ball speeds up when after striking player tiles, slowing slightly when colliding with the top and bottom walls
- The ball resets automatically on won point and direction is randomised. Speed resets with new ball.

### Controls
- Player 1 (left) W/S/Q = Up / Down / Cycle color
- Player 2 (right) UP/DOWN/LEFT = Up / Down / Cycle color

## Developers notes

This was my first project. I intended to write something that I knew I could do myself with minimal external input. I took concepts I learned in the asteroids chapter and replicated them here. I struggled to implement classes and inheritance. Instead I fell back on a single file structure, which worked fine for my purposes. 

What I was able to practice:
- Object initialisation
- Player controlled effects
- Non-player controlled effects
- Standard python syntax

In future projects I will explore object oriented programming more thoroughly. 
Regarding this project I chose to not attempt anything more than I could reasonably manage as a total beginner. I was proud to implement a color matching feature that was suggested to me by Juniper Dev on YouTube, and to have a working score count that ends the game when a player wins. 
Of the code I designed, I would estimate I used search engines and ChatGPT likes for 25%, mainly to improve and check syntax and to support my concept stage.

In conclusion, the project was basic, but satisfying, and a good place to start. If I update this project further I would like to use a split ball function to have multiple game balls to add a new layer of difficulty.