class NQBacktracking:
    def __init__(self, N, x_, y_):
        self.N = N
        self.x = x_
        self.y = y_
        self.ld = [0] * (2 * N - 1)
        self.rd = [0] * (2 * N - 1)
        self.cl = [0] * N
        self.solutions = []

    def printSolutions(self):
        for idx, solution in enumerate(self.solutions, 1):
            print(f"Solution Number {idx}: ")
            for i in range(self.N):
                for j in range(self.N):
                    if solution[i][j] == 1:
                        print('Q', end=' ')
                    else:
                        print('_', end=' ')
                print()
            print()
        print(f"Total {len(self.solutions)} solutions found.")
    
    def solveNQUtil(self, board, col):
        if col >= self.N:
            # Copy the board to the list of solutions
            self.solutions.append([row[:] for row in board])
            return False  # Change this line to search for all solutions
        if col == self.y:
            return self.solveNQUtil(board, col + 1)
        for i in range(self.N):
            if i == self.x:
                continue
            if (self.ld[i - col + self.N - 1] != 1 and self.rd[i + col] != 1) and self.cl[i] != 1:
                board[i][col] = 1
                self.ld[i - col + self.N - 1] = self.rd[i + col] = self.cl[i] = 1
                # Continue searching for more solutions
                self.solveNQUtil(board, col + 1)
                # Backtrack
                board[i][col] = 0
                self.ld[i - col + self.N - 1] = self.rd[i + col] = self.cl[i] = 0
        return False
    
    def solveNQ(self):
        board = [[0 for _ in range(self.N)] for _ in range(self.N)]
        board[self.x][self.y] = 1
        self.ld[self.x - self.y + self.N - 1] = self.rd[self.x + self.y] = self.cl[self.x] = 1
        self.solveNQUtil(board, 0)
        if not self.solutions:
            print("No solution exists")
        else:
            self.printSolutions()

# Parameters for the N-Queens problem
N = int(input("Enter size of board: "))  # Size of the chessboard
x = int(input("Enter the row of initial position of first queen: "))  # Row for the initial position of the 1st queen
y = int(input("Enter the column of initial position of first queen: "))  # Column for the initial position of the 1st queen

# Initialize the NQBacktracking class with the parameters
NQBt = NQBacktracking(N, x, y)
# Execute the solveNQ method to find and print all solutions
NQBt.solveNQ()