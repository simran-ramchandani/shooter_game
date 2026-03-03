# 2D Shooter Game (Python)

This project is a 2D space shooter game developed in Python. The game
features a player-controlled spaceship that shoots enemies, avoids
collisions, and scores points by eliminating incoming alien ships.

The project demonstrates game development fundamentals including
animation, collision detection, sound integration, and event handling.

------------------------------------------------------------------------

## Project Overview

The player controls a spaceship that can:

-   Move horizontally across the screen
-   Shoot bullets at incoming enemies
-   Avoid alien attacks
-   Score points by destroying enemies

Enemies descend from the top of the screen, and the game ends if they
reach a certain threshold or collide with the player.

------------------------------------------------------------------------

## Technologies Used

-   Python
-   Pygame library
-   PNG image assets
-   WAV sound effects

------------------------------------------------------------------------

## Project Files

-   `gaming.py` -- Main game logic and execution file
-   `spaceship.png` -- Player sprite
-   `alien1.png` to `alien5.png` -- Enemy sprites
-   `bullet.png` -- Player bullet
-   `alien_bullet.png` -- Enemy projectile
-   `bg.png` -- Background image
-   `explosion.wav`, `explosion2.wav`, `laser.wav` -- Sound effects

------------------------------------------------------------------------

## Features

-   Real-time keyboard controls
-   Enemy spawning and movement
-   Bullet firing mechanism
-   Collision detection system
-   Score tracking
-   Background music and sound effects
-   Explosion animation

------------------------------------------------------------------------

## How to Run

1.  Install Pygame:

        pip install pygame

2.  Navigate to the project directory.

3.  Run the game:

        python gaming.py

------------------------------------------------------------------------

## Controls

-   Left Arrow -- Move left
-   Right Arrow -- Move right
-   Spacebar -- Shoot

------------------------------------------------------------------------

## Learning Outcomes

This project demonstrates:

-   Object interaction in games
-   Game loop implementation
-   Handling user input events
-   Sprite animation and rendering
-   Audio integration
-   Basic game physics and collision detection

------------------------------------------------------------------------

## Future Improvements

-   Add levels and increasing difficulty
-   Add health system
-   Add power-ups
-   Improve enemy AI
-   Add start and game-over screens
-   Store high scores

------------------------------------------------------------------------

## Use Case

This project is suitable for showcasing beginner to intermediate game
development skills in Python and demonstrates practical use of the
Pygame library for interactive applications.
