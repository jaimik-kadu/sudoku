# Sudoku Game and Solver

## Description
This project is a comprehensive Sudoku game and solver application built using Python's Tkinter library. It allows users to play Sudoku puzzles of varying difficulty levels or solve their own custom Sudoku puzzles using the built-in solver.

---

## Features

### Game Mode:
1. **New Game:** Start a new Sudoku puzzle.
2. **Difficulty Levels:** Choose between Easy, Medium, or Hard puzzles.
3. **Live Validation:** Automatically checks entries to ensure they adhere to Sudoku rules.
4. **Completion Check:** Validates the user's solution upon completion.

### Solver Mode:
1. **Input Custom Puzzle:** Enter a custom 9x9 grid.
2. **Automatic Solving:** Solve the puzzle instantly.
3. **Error Handling:** Alerts users if a solution does not exist.

### Additional Features:
1. **Instructions and Rules:** Provides step-by-step gameplay instructions and Sudoku rules.
2. **Clear and Reset:** Reset the board to start fresh.

---

## Prerequisites

- Python 3.6+
- Tkinter (standard library in Python)

---

## How to Run

1. Clone or download this repository.
2. Ensure the required dependencies are installed.
3. Run the `main.py` file using Python:

   ```bash
   python main.py
   ```

4. Follow the on-screen instructions to play or solve Sudoku.

---

## Usage

### Main Menu:
- **New Game:** Select this to start a new puzzle.
- **Sudoku Solver:** Use this to solve your custom puzzle.
- **Rules:** Learn about Sudoku rules.
- **Instructions:** Understand how to play Sudoku.

### Game Controls:
- **Main Menu:** Return to the main menu.
- **Back:** Navigate back to the previous screen.
- **Reset:** Clear the current puzzle.
- **Solve:** Automatically solve the entered Sudoku puzzle.

---

## Code Highlights

### Sudoku Solver:
The `solve_sudoku` function uses a backtracking algorithm to find solutions for a given Sudoku puzzle.

### Board Generation:
The `create_puzzle` function generates Sudoku puzzles of varying difficulty levels using a randomized approach.

### GUI Implementation:
The application leverages Tkinter's `Frame`, `Label`, and `Entry` widgets to create an intuitive user interface.

---

## Rules of Sudoku
1. Each row of the 9x9 grid must contain all the digits from 1 to 9 without repetition.
2. Each column of the 9x9 grid must contain all the digits from 1 to 9 without repetition.
3. Each of the nine 3x3 sub-grids must contain all the digits from 1 to 9 without repetition.

---

## Future Enhancements
1. Add support for saving and loading games.
2. Include a timer for tracking puzzle completion time.
3. Implement hints for assisting players.

---

## Acknowledgments
This project was developed using the Python programming language and the Tkinter library for GUI development. Sudoku puzzles are randomly generated for an engaging user experience.
