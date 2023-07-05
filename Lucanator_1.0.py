class Board:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        self.currentPlayer = "w"

    
    def move_piece(self, move):
        start_pos = move[:2]
        end_pos = move[2:]

        start_row, start_col = self.get_row_col(start_pos)
        end_row, end_col = self.get_row_col(end_pos)
        
        piece = self.board[start_row][start_col]

        if piece == "-":
            return False
        
        if piece != self.currentPlayer:
            return False

        if piece == "wP" or "bP":
            validPawn(start_row, start_col, end_row, end_col, piece)
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = "-"

        self.currentPlayer = "b" if self.currentPlayer == "w" else "w"

#Missing promotion and En Passant atm
def validPawn(start_row, start_col, end_row, end_col, piece):
        if piece == "bP":
            if start_col == end_col:
                if end_row == start_row + 1 and piece[end_row] == "-":
                    return True
                elif start_row == 1 and end_row == 3 and piece[end_row] == "-" and piece[end_row - 1] == "-":
                    return True
        if piece == "wP":
            if start_col == end_col:
                if end_row == start_row - 1 and piece[end_row] == "-":
                    return True
                elif start_row == 6 and end_row == 4 and piece[end_row] == "-" and piece[end_row + 1] == "-":
                    return True
            elif end_col == start_col +- 1:
                if piece == "pB" and start_row + 1 == end_row:
                    return True
                elif piece == "wP" and start_row - 1 == end_row:
                    return True
                else:
                    return False

# Will be implemented soon
def validRook(start_row, start_col, end_row, end_col, piece):
    if piece == "bR":
        print("")
    if piece == "wR":
        print("")

def print_board(board):
    for row in board:
        for piece in row:
            print('{:<3}'.format(piece), end='')
        print()
