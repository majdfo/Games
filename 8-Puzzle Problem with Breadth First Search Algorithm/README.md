# 8-Puzzle Solver using Breadth-First Search (BFS)

## Assignment 1: Solving 8-Puzzle Problem with BFS Algorithm

### Overview
This project implements an optimal solution for the **8-Puzzle Problem** using the **Breadth-First Search (BFS) algorithm** in Python. The solution explores possible moves in a breadth-first manner to find the shortest path to the goal state.

---

## 8-Puzzle Problem
The **8-Puzzle Problem** is a sliding tile puzzle consisting of a **3x3 grid** containing tiles numbered **1 to 8** and a **blank space (0)**. The objective is to rearrange the tiles from any given initial configuration to the **goal state**:

```
1 2 3
4 5 6
7 8 0
```

The blank tile (0) can be swapped with an adjacent tile (left, right, up, or down).

### Features
- **BFS Algorithm:** Ensures an optimal solution by exploring all possible moves level by level.
- **Graphical User Interface (GUI):** Allows users to input an initial puzzle state and visualize the solution step by step.
- **Solution Output:** Saves the solution steps to a text file (`solution_states.txt`).
- **Error Handling:** Validates user input and displays appropriate messages for invalid entries.
- **Bonus Feature:** Displays tile movements dynamically in the GUI.

---

## Implementation Details
### Algorithm
1. Start with the initial puzzle state provided by the user.
2. Use a **queue (FIFO)** to explore states in a breadth-first manner.
3. Keep track of **visited states** to prevent redundant calculations.
4. Store the path (sequence of moves) leading to the goal state.
5. Display the solution in the GUI and save it to a file.

### Data Structures Used
- **Queue (`collections.deque`)**: Manages the BFS search frontier.
- **Set (`visited`)**: Stores visited states to prevent cycles.
- **Graph Representation**: Each state is treated as a node in a graph.

### GUI Components
- **Input Grid:** Users enter the initial puzzle configuration.
- **Solve Button:** Triggers the BFS solution.
- **Step-by-Step Solution Display:** Shows the sequence of moves.
- **Graphical Tile Movement:** Animates tile transitions.

---

## Getting Started
### Prerequisites
Ensure you have **Python 3.x** installed along with the following libraries:
```sh
pip install tk
```

### Running the Program
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/8puzzle-bfs.git
   cd 8puzzle-bfs
   ```
2. Run the Python script:
   ```sh
   python puzzle_solver.py
   ```
3. Enter the **initial puzzle configuration** in the GUI.
4. Click **Solve :)** to find the optimal solution.

---

## Example Usage
### Sample Input (Initial State):
```
5 2 7
8 4 0
1 3 6
```

### Sample Output (Solution Steps):
```
Step 1: Move Blank Down
Step 2: Move Blank Right
Step 3: Move Blank Up
...
```

The solution is also stored in `solution_states.txt`.

---

## File Structure
```
8puzzle-bfs/
│── puzzle_solver.py  # Main script implementing BFS and GUI
│── solution_states.txt  # File storing solution steps
│── README.md  # Project documentation
```

---

## Limitations
- The BFS approach guarantees an optimal solution but may be **slow for highly complex states**.
- The GUI requires **Tkinter**, which may not work in some environments without proper configuration.

---

## Future Enhancements
- Implementing **A* Search Algorithm** for better performance.
- Adding **heuristic-based optimizations**.
- Improving GUI aesthetics.

 
