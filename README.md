# JetpackJoyride
This is a very basic replica of Jetpack Joyride that runs on terminal. It is written in Python3 and no external libraries like pygame were used. It uses ASCII characters.

## Description Of Classes
- Back: This class creates a 54x2000 board with boundaries.
- Bullet: This class creates bullets.
- Enemy: This class creates our enemy and initializes its position.
- Person: This class creates the main character of the game.
- Magnet: This class generates magnets at random positions.
- Obstacle: This class generates obstacles at random positions.
- Main: This incorporates all classes and run the game.

## How to play
- Install libraries like colorama and numpy with `pip3 install [module name]`.
- Run `python3 main.py` to start the game.
- Press 'a' to move left, 'w' to activate jetpack, 's' to move downwards, 'd' to move right, 'j' to fire bullets and spacebar to activate the shield.
- Press 'q' to quit the game.

## Requirements
- Python3

## Features
- Fire Beams: Appear as obstacles through the course of the game.
- Shield: Activated using spacebar. It lasts 10 seconds and then takes 60 seconds to refill again after use.
- Speed Boost: Speed of the game will increase upon taking this power-up.
- Magnet: Appears on the way and influence the motion of the Mandalorian.
