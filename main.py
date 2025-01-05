from tkinter import *
from tkinter import messagebox
import random

# User Input
def user_find_empty(pzl):

    for row in range(9):
        for col in range(9):
            if pzl[row][col] == 0:
                return (row, col)
    return None


def user_is_valid(pzl, guess, row, col):

    row_vals = pzl[row]
    if guess in row_vals:
        return False

    col_vals = [pzl[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if pzl[i][j] == guess:
                return False

    return True


def user_solve_sudoku(pzl):

    empty_cell = user_find_empty(pzl)
    if not empty_cell:
        return True

    row, col = empty_cell
    for guess in range(1, 10):
        if user_is_valid(pzl, guess, row, col):
            pzl[row][col] = guess
            if user_solve_sudoku(pzl):
                return True
            pzl[row][col] = 0

    return False

# End


def find_empty(puzzle):

    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return (row, col)
    return None


def is_valid_number(puzzle, guess, row, col):

    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if puzzle[i][j] == guess:
                return False
    return True


def is_valid_sudoku_board(puzzle):
    # Check rows
    for row in puzzle:
        if not is_valid_set(row):
            return False

    # Check columns
    for col in range(9):
        column = [puzzle[row][col] for row in range(9)]
        if not is_valid_set(column):
            return False

    # Check boxes
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            box = [puzzle[r][c]
                   for r in range(row, row + 3) for c in range(col, col + 3)]
            if not is_valid_set(box):
                return False

    # If all checks pass, the board is valid
    return True


def is_valid_set(nums):
    """
    Helper function to check if a set of 9 numbers is valid for Sudoku
    """
    nums = [n for n in nums if n != 0]
    return len(nums) == len(set(nums))


def solve_sudoku(puzzle):
    if is_valid_sudoku_board(puzzle):
        empty_cell = find_empty(puzzle)
        if not empty_cell:
            return True
        row, col = empty_cell
        for guess in range(1, 10):
            if is_valid_number(puzzle, guess, row, col):
                puzzle[row][col] = guess
                if solve_sudoku(puzzle):
                    return True
                puzzle[row][col] = 0
        return False
    else:
        return False

# Button to solve the Sudoku puzzle
def btnsolve():
    global puzzle
    global puzzle_entry
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                if puzzle_entry[i][j].get() == '':
                    puzzle[i][j] = 0
                else:
                    puzzle[i][j] = int(puzzle_entry[i][j].get())
    if solve_sudoku(puzzle):
        for i in range(9):
            for j in range(9):
                puzzle_entry[i][j].delete(0, END)
                puzzle_entry[i][j].insert(0, str(puzzle[i][j]))
    else:
        messagebox.showerror('Error', 'No solution exists for this puzzle.')


# Display the Rules for playing Sudoku
def rules():
    for widget in mainframe.winfo_children():
        widget.destroy()
    LblTitle.config(text="Rules")
    Button(mainframe, text="Back", height=1, width=10,
           bd=10, font=20, command=btnback).place(x=10, y=10)
    Label(mainframe, text="1. Each row of the 9x9 grid must contain all the digits from 1 to 9 without any repetition.",
          font=("Arial", 12, "bold")).place(x=50, y=120)
    Label(mainframe, text="2. Each column of the 9x9 grid must contain all the digits from 1 to 9 without any repetition.",
          font=("Arial", 12, "bold")).place(x=50, y=170)
    Label(mainframe, text="3. Each of the nine 3x3 sub-grids must contain all the digits from 1 to 9 without any repetition.",
          font=("Arial", 12, "bold")).place(x=50, y=220)


# Display the instructions for playing Sudoku
def instructions():

    for widget in mainframe.winfo_children():
        widget.destroy()

    LblTitle.config(text="Instructions")

    Button(mainframe, text="Back", height=1, width=10, bd=10, font=20, command=btnback).place(x=10, y=10)

    Label(mainframe, text="1. Start with a partially filled 9x9 grid with some numbers filled in.", font=("Arial", 12, "bold")).place(x=50, y=100)
    Label(mainframe, text="2. Fill each empty cell with a number from 1 to 9 without repetition in rows, columns, and regions.", font=("Arial", 12, "bold")).place(x=50, y=150)
    Label(mainframe, text="3. Identify rows, columns, and regions with few missing digits and fill them first.", font=("Arial", 12, "bold")).place(x=50, y=200)
    Label(mainframe, text="4. As more digits are filled, it becomes easier to identify missing digits in other areas.", font=("Arial", 12, "bold")).place(x=50, y=250)
    Label(mainframe, text="5. Solve using logical reasoning and deduction, avoid guessing to prevent errors.", font=("Arial", 12, "bold")).place(x=50, y=300)
    Label(mainframe, text="6. Successfully solve the Sudoku puzzle by filling in all missing digits.", font=("Arial", 12, "bold")).place(x=50, y=350)


# Function to clear the sudoku solver
def btnclear():

    global puzzle
    global puzzle_entry
    for i in range(9):
        for j in range(9):
            puzzle[i][j] = 0
            puzzle_entry[i][j].delete(0, END)

# Function to go back to the Main Menu
def btnback():

    for widget in mainframe.winfo_children():
        widget.destroy()
    b1 = Button(mainframe, text="New Game", height=2, width=23, bd=10, font=20, command=new_game)
    b1.place(x=265, y=30)
    b2 = Button(mainframe, text="Sudoku Solver", height=2, width=23, bd=10, font=20, command=solver)
    b2.place(x=265, y=120)
    b3 = Button(mainframe, text="Rules", height=2, width=23, bd=10, font=20, command=rules)
    b3.place(x=265, y=210)
    b4 = Button(mainframe, text="Instructions", height=2, width=23, bd=10, font=20, command=instructions)
    b4.place(x=265, y=300)
    LblTitle.config(text="Sudoku - The Ultimate Brain Teaser")

# Validate the entries inside the solver
def validate_entry(value):
    
    try:
        return value.isdigit() and int(value) in range(1, 10) or value == ""
    except ValueError:
        return False


def create_board():

    board = [[0 for x in range(9)] for y in range(9)]
    return board

# Filling in the numbers for the puzzle
def fill_board(board):

    numbers = list(range(1, 10))
    random.shuffle(numbers)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if fill_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

# To check if the puzzle provided to the user actually has a solution or not
def is_valid(board, row, col, num):

    for i in range(len(board)):
        if board[row][i] == num:
            return False
    for i in range(len(board[0])):
        if board[i][col] == num:
            return False
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    return True

# Function determines the difficulty level of the puzzle
def remove_cells(board, difficulty):

    cells_to_remove = 0
    if difficulty == "easy":
        cells_to_remove = 35
    elif difficulty == "medium":
        cells_to_remove = 45
    elif difficulty == "hard":
        cells_to_remove = 55
    for i in range(cells_to_remove):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while board[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        temp = board[row][col]
        board[row][col] = 0
        if not has_unique_solution(board):
            board[row][col] = temp

# To check if the sudoku has a unique solution
def has_unique_solution(board):

    board_copy = [row[:] for row in board]
    count = [0]
    solve(board_copy, count)
    if count[0] != 1:
        return False
    return True

def solve(board, count):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        solve(board, count)
                        board[i][j] = 0
                return
    count[0] += 1

# Creates the board of the game
def create_puzzle(difficulty):

    board = create_board()
    fill_board(board)
    remove_cells(board, difficulty)
    return board

# Function to check if user has succesfully completed the puzzle.
def check_entries(event):

    global sudoku_board
    filled = True
    for row in sudoku_board:
        for entry in row:
            if not entry.get():
                filled = False
                break
        if not filled:
            break

    if filled:
        # print(sudoku_board)
        input = []
        for row in sudoku_board:
            row_values = []
            for entry in row:
                value = entry.get()
                row_values.append(int(value))
            input.append(row_values)
        # print(input)
        if input == pzl_arr:
            response = messagebox.showinfo(
                "Congratulations!", "You have successfully completed the Sudoku puzzle!")
            if response == "ok":
                btnback()
        else:
            response = messagebox.showerror(
                "Unfortunately", "Your solution to the Sudoku puzzle is incorrect.")
            if response == "ok":
                btnback()

# Function to generate the game board for user to solve
def display_board(board):

    global sudoku_board, label

    Button(mainframe, text="Main Menu", height=1, width=10, bd=10, font=20, command=btnback).place(x=10, y=10)
    Sudoku_Frame = Frame(mainframe, bg='black', padx=5, pady=5)
    Sudoku_Frame.place(x=225, y=10)
    sudoku_board = []

    for i in range(9):
        row = []
        for j in range(9):
            cell_value = board[i][j]
            entry = Entry(Sudoku_Frame, width=2, font=("Arial", 24), justify="center")
            if cell_value == 0:
                entry.grid(row=j, column=i)
                entry.bind('<KeyRelease>', check_entries)
            else:
                entry.insert(0, cell_value)
                entry.configure(state="disabled")
                entry.grid(row=j, column=i)
            board[i][j] = entry
            row.append(entry)
        sudoku_board.append(row)


def easy():
    global pzl, pzl_arr
    for widget in mainframe.winfo_children():
        widget.destroy()
    LblTitle.config(text="Difficulty Level: Easy")
    board = create_puzzle('easy')
    display_board(board)

    # Puzzle given to user
    user_input = []
    for row in board:
        row_values = []
        for entry in row:
            value = entry.get()
            if value == '':
                row_values.append(0)
            else:
                row_values.append(int(value))
        user_input.append(row_values)
    # print(user_input)

    # Solution of puzzle given to user
    pzl = user_input
    pzl_arr = []
    if user_solve_sudoku(pzl):
        for row in pzl:
            pzl_arr.append(row)
    # print(pzl_arr)


def medium():

    global pzl, pzl_arr
    for widget in mainframe.winfo_children():
        widget.destroy()
    LblTitle.config(text="Difficulty Level: Medium")
    board = create_puzzle('medium')
    display_board(board)
    
    # Puzzle given to user
    user_input = []
    for row in board:
        row_values = []
        for entry in row:
            value = entry.get()
            if value == '':
                row_values.append(0)
            else:
                row_values.append(int(value))
        user_input.append(row_values)
    # print(user_input)

    # Solution of puzzle given to user
    pzl = user_input
    pzl_arr = []
    if user_solve_sudoku(pzl):
        for row in pzl:
            pzl_arr.append(row)
    # print(pzl_arr)


def hard():

    global pzl, pzl_arr
    for widget in mainframe.winfo_children():
        widget.destroy()
    LblTitle.config(text="Difficulty Level: Hard")
    board = create_puzzle('hard')
    display_board(board)

    # Puzzle given to user
    user_input = []
    for row in board:
        row_values = []
        for entry in row:
            value = entry.get()
            if value == '':
                row_values.append(0)
            else:
                row_values.append(int(value))
        user_input.append(row_values)
    # print(user_input) 

    # Solution of puzzle given to user
    pzl = user_input
    pzl_arr = []
    if user_solve_sudoku(pzl):
        for row in pzl:
            pzl_arr.append(row)
    # print(pzl_arr)


def new_game():

    # Destroy all child widgets of the mainframe.
    for widget in mainframe.winfo_children():
        widget.destroy()
    
    LblTitle.config(text="Select Difficulty Level")
    
    # Buttons to select difficulty level.
    Button(mainframe, text="Back", height=1, width=10, bd=10, font=20, command=btnback).place(x=10, y=10)
    Button(mainframe, text="Easy", height=2, width=23, bd=10, font=20, command=easy).place(x=265, y=50)
    Button(mainframe, text="Medium", height=2, width=23, bd=10, font=20, command=medium).place(x=265, y=150)
    Button(mainframe, text="Hard", height=2, width=23, bd=10, font=20, command=hard).place(x=265, y=250)


def solver():

    global puzzle
    global puzzle_entry
    
    # Destroy all child widgets of the mainframe.
    for widget in mainframe.winfo_children():
        widget.destroy()

    LblTitle.config(text="Sudoku Solver")

    # Creates a frame-in-frame for sudoku grid to take input from the user.
    Sudoku_Frame = Frame(mainframe, bg='black', padx=5, pady=5)
    Sudoku_Frame.place(x=165, y=40)

    # Creating and placing cells of the grid inside the sudoku frame.
    puzzle = [[0 for i in range(9)] for j in range(9)]
    puzzle_entry = [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            puzzle_entry[i][j] = Entry(Sudoku_Frame, width=3, font='Arial 20 bold', justify='center', validate="key", validatecommand=(Sudoku_Frame.register(validate_entry), "%S"))
            puzzle_entry[i][j].grid(row=i, column=j)

    # Buttons for the Solver
    Button(mainframe, text="Back", height=1, width=10, bd=10, font=20, command=btnback).place(x=10, y=40)
    Button(mainframe, text="Reset", height=1, width=10, bd=10, font=20, command=btnclear).place(x=625, y=40)
    Button(mainframe, text="Solve", height=1, width=10, bd=10, font=20, command=btnsolve).place(x=625, y=120)


def main_screen():

    global mainframe
    global LblTitle

    # Creates a new tkinter window with a specific size, position, and title, and sets an image as the window icon.
    screen = Tk()
    screen.geometry("1280x720+150+80")
    screen.title("Sudoku - The Ultimate Brain Teaser")
    image_icon = PhotoImage(file='logo.png')
    screen.iconphoto(False, image_icon)

    # Sets up the game window by creating a title label, a border frame, and a main frame.
    LblTitle = Label(text="Sudoku - The Ultimate Brain Teaser", font=("arial", 50, 'bold'), fg="black")
    LblTitle.pack(pady=50)
    bordercolor = Frame(screen, bg='black', width=800, height=400)
    bordercolor.pack()
    mainframe = Frame(bordercolor, width=800, height=400)
    mainframe.pack(padx=20, pady=20)
    
    # Buttons for the main frame
    b1 = Button(mainframe, text="New Game", height=2, width=23, bd=10, font=20, command=new_game)
    b1.place(x=265, y=30)
    b2 = Button(mainframe, text="Sudoku Solver", height=2, width=23, bd=10, font=20, command=solver)
    b2.place(x=265, y=120)
    b3 = Button(mainframe, text="Rules", height=2, width=23, bd=10, font=20, command=rules)
    b3.place(x=265, y=210)
    b4 = Button(mainframe, text="Instructions", height=2, width=23, bd=10, font=20, command=instructions)
    b4.place(x=265, y=300)
    
    screen.mainloop()

main_screen()