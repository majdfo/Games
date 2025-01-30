# Tic-Tac-Toe with Minimax Algorithm

This project is an implementation of Tic-Tac-Toe with an AI opponent that plays optimally using the Minimax algorithm. The AI ensures that it never loses and will either win or force a tie if both players play optimally.

## Overview
This project is based on the CS50 course at Harvard University. It involves implementing an AI for Tic-Tac-Toe using Minimax to determine the best possible move for a given board state.

## Features
- **Minimax Algorithm**: AI determines the optimal move for the current player.
- **Graphical Interface**: Built using `pygame` for an interactive experience.
- **Automatic AI Moves**: The computer plays optimally and makes its moves automatically.
- **Support for Two Players**: Play against the AI or manually take turns.

## Requirements
- Python 3.10+
- `pygame` package (for GUI support)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/tictactoe-minimax.git
   cd tictactoe-minimax
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## How to Play
1. Run the game using:
   ```sh
   python runner.py
   ```
2. Select your player (`X` or `O`).
3. The game will start, and you will take turns with the AI.
4. The AI will make optimal moves using Minimax.
5. The game ends when a player wins or the board is full (tie).
6. Option to restart after each game.

## Code Structure
- **`tictactoe.py`**: Implements the logic for Tic-Tac-Toe, including Minimax.
- **`runner.py`**: Handles the graphical interface and user interactions.

## Minimax Algorithm Implementation
The Minimax function works as follows:
- **`minimax(board)`**: Determines the best move for the current player.
- **`max_value(board)`**: Evaluates the maximum utility for the AI player (`X`).
- **`min_value(board)`**: Evaluates the minimum utility for the opponent (`O`).
- **Recursive evaluation** ensures the AI chooses the best move.

## Winning Conditions
A player wins if they have three of their marks in a row, column, or diagonal.

## Notes
- The AI cannot be beaten due to the nature of Minimax.
- Alpha-beta pruning can be added to improve efficiency (optional).

 
