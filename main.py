
import tkinter as tk

class SudokuSolverGUI:
    def __init__(self, board):
        self.board = board

        # Initialize the GUI
        self.window = tk.Tk()
        self.window.title("Sudoku Solver")
        self.create_widgets()

    def create_widgets(self):
        # Create the board frame
        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()

        # Create the board cells
        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                cell = tk.Entry(self.board_frame, width=2, font=("Arial", 20))
                cell.grid(row=i, column=j, padx=1, pady=1)
                cell.insert(0, str(self.board[i][j]))
                row.append(cell)
            self.cells.append(row)

        # Create the solve button
        self.solve_button = tk.Button(self.window, text="Solve", command=self.solve_board)
        self.solve_button.pack()

        # Create the message box
        self.message_box = tk.Message(self.window, text="")
        self.message_box.pack()

    def solve_board(self):
        # Get the board values from the cells
        for i in range(9):
            for j in range(9):
                value = self.cells[i][j].get()
                if value == "":
                    self.board[i][j] = 0
                else:
                    self.board[i][j] = int(value)

        # Solve the board
        solve_sudoku(self.board)

        # Update the cells with the solution
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].insert(0, str(self.board[i][j]))

        # Show a message indicating if the board was solved or not
        if is_valid_solution(self.board):
            self.message_box.config(text="Board solved!")
        else:
            self.message_box.config(text="Board not solvable")

    def run(self):
        self.window.mainloop()

# Example Sudoku puzzle
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Create and run the Sudoku solver GUI
gui = SudokuSolverGUI(board)
gui.run()
