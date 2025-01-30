import tkinter as tk
from tkinter import messagebox
from collections import deque

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

class BFS:
    def __init__(self):
        self.queue = deque()
        self.visited = set()

    def find_zero(self, puzzle):
        for i in range(3):
            for j in range(3):
                if puzzle[i][j] == 0:
                    return i, j

    def get_moves(self, puzzle):
        moves = []
        zero_i, zero_j = self.find_zero(puzzle)
        if zero_i > 0:
            moves.append((-1, 0, 'Up'))    # up
        if zero_i < 2:
            moves.append((1, 0, 'Down'))   # down
        if zero_j > 0:
            moves.append((0, -1, 'Left'))  # left
        if zero_j < 2:
            moves.append((0, 1, 'Right'))  # right
        return moves

    def make_move(self, puzzle, move):
        zero_i, zero_j = self.find_zero(puzzle)
        new_puzzle = [row[:] for row in puzzle] # deepcopy
        dx, dy, _ = move
        new_puzzle[zero_i][zero_j], new_puzzle[zero_i + dx][zero_j + dy] = new_puzzle[zero_i + dx][zero_j + dy], new_puzzle[zero_i][zero_j] # swap
        return new_puzzle

    def pstring(self, puzzle):
        return "".join(str(cell) for row in puzzle for cell in row)

    def solve(self, initial_state, goal_state):
        self.queue.append((initial_state, []))  # initial state and an empty path

        solutions = []

        while self.queue:
            current_state, path = self.queue.popleft()

            if current_state == goal_state:
                solutions.append(path)  # solution steps

                with open("solution_states.txt", "w") as file:
                    for step in path:
                        file.write(f"{step}\n")

                return path

            self.visited.add(tuple(map(tuple, current_state)))  # Add current state to visited states

            for move in self.get_moves(current_state):
                new_state = self.make_move(current_state, move)
                if tuple(map(tuple, new_state)) not in self.visited:
                    self.queue.append((new_state, path + [move]))

        return None

class PuzzleSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("8Puzzle Solver")
        self.root.configure(bg='pink')
        # input
        self.input_frame = tk.Frame(self.root, bg='pink')
        self.input_frame.pack(pady=10)
        # boxes for input
        self.ent = []
        for i in range(3):
            for j in range(3):
                e = tk.Entry(self.input_frame, width=5, font=('Arial', 20))
                e.grid(row=i, column=j, padx=3, pady=3)
                self.ent.append(e)

        # Solve button
        self.solve_button = tk.Button(self.root, text=" Solve :)", command=self.solve_puzzle, font=('Arial', 14), bg='white')
        self.solve_button.pack(pady=5)

        # steps
        self.puzzle_display = tk.Canvas(self.root, width=150, height=150, bg='white')
        self.puzzle_display.pack()
        self.steps_text = tk.Text(self.root, width=30, height=10, wrap=tk.WORD, bg='white', fg='black')
        self.steps_text.pack()
        self.steps_text.pack()
        self.bfs = BFS()

    def solve_puzzle(self):
        initial_state = []
        for i in range(3):
            row_values = [self.ent[i * 3 + j].get() for j in range(3)]
            if '' in row_values:
                messagebox.showerror("Input Error", "Please fill in all the puzzle values.")
                return
            initial_state.append([int(value) for value in row_values])

        goal_state = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]

        solution = self.bfs.solve(initial_state, goal_state)

        if solution:
            self.move_tiles(initial_state, solution)
            self.show_solution_steps(solution)
        else:
            messagebox.showinfo("No Solution", "No solution exists for the provided puzzle ):")

    def move_tiles(self, initial_state, solution):
        colors = {0: "yellow"}

        for move in solution:
            zero_i, zero_j = self.bfs.find_zero(initial_state)
            dx, dy, _ = move
            initial_state[zero_i][zero_j], initial_state[zero_i + dx][zero_j + dy] = initial_state[zero_i + dx][zero_j + dy], initial_state[zero_i][zero_j]

            self.draw_puzzle(self.puzzle_display, initial_state, colors)
            self.root.update()
            self.root.after(1000)

    def show_solution_steps(self, solution):
        for i, step in enumerate(solution, start=1):
            self.steps_text.insert(tk.END, f"Step {i}: {step}\n")

    def draw_puzzle(self, canvas, puzzle, colors):
        canvas.delete("all")
        for i in range(3):
            for j in range(3):
                x0, y0 = j * 50, i * 50
                x1, y1 = x0 + 50, y0 + 50
                color = colors.get(puzzle[i][j], "white")
                canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black", width=3)
                canvas.create_text(x0 + 25, y0 + 25, text=str(puzzle[i][j]), font=("Arial", 16))

if __name__ == "__main__":
    root = tk.Tk()
    game = PuzzleSolver(root)
    root.mainloop()
