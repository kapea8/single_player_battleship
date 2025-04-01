# Battleship Game - Python Command Line

## Description

This Python project implements a classic Battleship game played in the command line. The game features randomly placed ships on a grid, and the player attempts to sink them by guessing their locations. The game provides feedback on hits and misses, displays the game board, and tracks the number of remaining guesses.

## Features

* **Command-Line Interface (CLI):** Implemented using standard Python input and output for a straightforward text-based gaming experience.
* **Random Ship Placement:** Utilizes a separate `ships.py` module to randomly place ships on the game board, ensuring varied gameplay.
* **Grid-Based Gameplay:** Represents the game board as a 2D list, allowing for easy tracking of guesses and ship locations.
* **Hit/Miss Feedback:** Provides clear feedback to the player on each guess, indicating whether it was a hit or a miss.
* **Ship Sinking Detection:** Determines when a ship has been completely sunk and informs the player.
* **Color-coded display:** Uses the termcolor library to color hits red, and misses blue.
* **Guess Tracking:** Limits the number of guesses the player has, adding a challenge to the game.
* **Win/Lose Conditions:** Clearly defines and communicates the win and lose states to the player.
