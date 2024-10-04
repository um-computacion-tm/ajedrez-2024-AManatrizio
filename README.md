# Author: Antonella Manatrizio 


# CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-AManatrizio/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-AManatrizio/tree/main)

# Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/b881fe6f2b0d203478b7/maintainability)](https://codeclimate.com/github/um-computacion-tm/first-circleci-AManatrizio/maintainability)

# Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/b881fe6f2b0d203478b7/test_coverage)](https://codeclimate.com/github/um-computacion-tm/first-circleci-AManatrizio/test_coverage)



# Chess Game - Python Project

Welcome to the **Chess Game project**, built with Python. This project allows you to play a full game of chess or run tests to ensure everything works correctly. It also includes Docker to make it easy to run the game.

## Objective of the Game
**The main goals are:**
- Capture your opponent's king.
- Capture all of their pieces.
- The game can also end by mutual agreement between both players.

## Setup
- Chess is played on an 8x8 board.
- Each player starts with 16 pieces:
- **White pieces:** ♔ ♕ ♖ ♗ ♘ ♙
- **Black pieces:** ♚ ♛ ♜ ♝ ♞ ♟
- White always moves first.

## Movement Rules
- **King** (♔ / ♚): Moves one square in any direction.
- **Queen** (♕ / ♛): Moves any number of squares in any direction.
- **Rook** (♖ / ♜): Moves any number of squares horizontally or vertically.
- **Bishop** (♗ / ♝): Moves diagonally any number of squares.
- **Knight** (♘ / ♞): Moves in an "L" shape: two squares in one direction, then one square to the side.
- **Pawn** (♙ / ♟): Moves one square forward (or two squares on its first move) and captures diagonally.

### Special Moves
- **Promotion:** A pawn that reaches the other side of the board can be promoted to any other piece (except the king).

## How to Win
- **Capture the King:** The game ends when a player captures the opponent's king.
- **Capture All Pieces:** The game ends when one player captures all of their opponent's pieces.
- **Mutual Agreement:** The game can also end if both players agree to stop the game.

## How to Play Using Docker
### Prerequisites
- You need to have Docker installed.
- Steps to Run the Game in Docker
Clone the repository:

git clone https://github.com/um-computacion-tm/ajedrez-2024-AManatrizio.git
- Build the Docker image: In the project folder, run the following command to build the Docker image:

**docker build -t chess-game .**

- Run the game: To play the chess game interactively from the terminal, run:

**docker run -it chess-game**

### Running Tests
To run unit tests and see a coverage report, use this command:

**docker run -it chess-game coverage run -m unittest && coverage report -m**

This will run all tests using unittest and show a coverage report to see which parts of the code are tested.