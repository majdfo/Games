# Minesweeper AI

## Overview
This project is an AI-based Minesweeper solver implemented in Python, inspired by the CS50 course at Harvard University. The AI utilizes propositional logic to infer mine locations and make intelligent moves.

## Getting Started
### Prerequisites
Ensure you have Python installed on your system. You also need to install the required dependencies before running the project.

### Installation
1. Clone this repository to your local machine:
   ```sh
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```sh
   cd minesweeper-ai
   ```
3. Install dependencies:
   ```sh
   pip3 install -r requirements.txt
   ```

## How to Run
Once all dependencies are installed, you can run the game using:
```sh
python runner.py
```
This will launch a graphical interface where you can play Minesweeper manually or let the AI play.

## Game Description
Minesweeper is a grid-based puzzle game where some cells contain hidden mines. The objective is to flag all mines without clicking on them. Each revealed safe cell provides a count of neighboring mines, helping the player deduce safe and mined locations.

## AI Implementation
The AI uses logical inference to make safe moves, flag mines, and make educated guesses when necessary. 
### Knowledge Representation
The AI represents its knowledge using logical sentences of the form:
```python
{A, B, C, D, E, F, G, H} = 1
```
Where the left-hand side is a set of unknown cells, and the right-hand side is the number of mines among them.

### Inference Methods
- If a sentence has a count of 0, all its cells are safe.
- If the count equals the number of cells, all cells are mines.
- If one sentence is a subset of another, the AI derives new sentences to refine knowledge.

## Project Structure
- `runner.py` – Handles the graphical interface for the game.
- `minesweeper.py` – Contains logic for gameplay and AI decision-making.
- `requirements.txt` – Lists necessary Python packages.

### Key Classes
1. **Minesweeper** – Implements the game mechanics.
2. **Sentence** – Represents logical constraints.
3. **MinesweeperAI** – The AI agent that makes inferences and decides moves.

## Implementation  
 

### In `Sentence` class:
- `known_mines()` – Returns cells known to be mines.
- `known_safes()` – Returns cells known to be safe.
- `mark_mine(cell)` – Updates sentence when a mine is found.
- `mark_safe(cell)` – Updates sentence when a safe cell is found.

### In `MinesweeperAI` class:
- `add_knowledge(cell, count)` – Updates AI knowledge based on revealed information.
- `make_safe_move()` – Returns a known safe move if available.
- `make_random_move()` – Chooses a random move when no safe move is known.

## Hints
- `add_knowledge()` is the most complex function and should be implemented step by step.
- The AI will not always win, as some situations require guessing.
- Avoid modifying a set while iterating over it.

 

