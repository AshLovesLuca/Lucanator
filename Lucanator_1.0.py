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

    def get_promotion_piece(self, current_player):
        color = "w" if current_player == "w" else "b"
        promotion_options = ["Q", "R", "B", "N"]
        promotion_choice = input(f"Choose the promotion piece for {color} player (Q, R, B, N): ")

        piece_mapping = {
            "Q": f"{color}Q",
            "R": f"{color}R",
            "B": f"{color}B",
            "N": f"{color}N"
        }

        return piece_mapping.get(promotion_choice.upper(), f"{color}Q")

    


    def print_board(self):
        for row in self.board:
            for piece in row:
                print('{:<3}'.format(piece), end='')
            print()

    def move_piece(self, move):
        start_pos = move[:2]
        end_pos = move[2:4]  # Extract only the position part of the move string

        start_row, start_col = self.get_row_col(start_pos)
        end_row, end_col = self.get_row_col(end_pos)

        piece = self.board[start_row][start_col]

        if piece == "-":
            return False

        if piece != self.currentPlayer:
            return False

        if piece == "wP" or piece == "bP":
            if self.validPawn(start_row, start_col, end_row, end_col, piece):
                self.board[end_row][end_col] = piece
                self.board[start_row][start_col] = "-"
                self.currentPlayer = "b" if self.currentPlayer == "w" else "w"
                return True
            else:
                return False

        if piece == "wR" or piece == "bR":
            if self.validRook(start_row, start_col, end_row, end_col, piece):
                self.board[end_row][end_col] = piece
                self.board[start_row][start_col] = "-"
                self.currentPlayer = "b" if self.currentPlayer == "w" else "w"
                return True
            else:
                return False

        if piece == "wN" or piece == "bN":
            if self.validKnight(start_row, start_col, end_row, end_col, piece):
                self.board[end_row][end_col] = piece
                self.board[start_row][start_col] = "-"
                self.currentPlayer = "b" if self.currentPlayer == "w" else "w"
                return True
            else:
                return False

        if piece == "wB" or piece == "bB":
            if self.validBishop(start_row, start_col, end_row, end_col, piece):
                self.board[end_row][end_col] = piece
                self.board[start_row][start_col] = "-"
                self.currentPlayer = "b" if self.currentPlayer == "w" else "w"
                return True
            else:
                return False

        if piece == "wQ" or piece == "bQ":
            if self.validQueen(start_row, start_col, end_row, end_col, piece):
                self.board[end_row][end_col] = piece
                self.board[start_row][start_col] = "-"
                self.currentPlayer = "b"if self.currentPlayer == "w" else "w"
                return True
            else:
                return False

        if piece == "wK" or piece == "bK":
            if self.validKing(start_row, start_col, end_row, end_col, piece):
                self.board[end_row][end_col] = piece
                self.board[start_row][start_col] = "-"
                self.currentPlayer = "b" if self.currentPlayer == "w" else "w"
                return True
            else:
                return False

        return False

    def get_row_col(self, position):
        row = 8 - int(position[1])
        col = ord(position[0].lower()) - ord("a")
        return row, col

    def validPawn(self, start_row, start_col, end_row, end_col, piece):
        if piece == "bP":
            if start_col == end_col:
                if end_row == start_row + 1 and self.board[end_row][end_col] == "-":
                    return True
                elif start_row == 1 and end_row == 3 and self.board[end_row][end_col] == "-" and self.board[end_row - 1][end_col] == "-":
                    return True
            elif abs(start_col - end_col) == 1 and end_row == start_row + 1 and self.board[end_row][end_col][0] == "w":
                return True
        elif piece == "wP":
            if start_col == end_col:
                if end_row == start_row - 1 and self.board[end_row][end_col] == "-":
                    return True
                elif start_row == 6 and end_row == 4 and self.board[end_row][end_col] == "-" and self.board[end_row + 1][end_col] == "-":
                    return True
            elif abs(start_col - end_col) == 1 and end_row == start_row - 1 and self.board[end_row][end_col][0] == "b":
                return True
        return False






    def validRook(self, start_row, start_col, end_row, end_col, piece):
        if piece == "bR" or piece == "wR":
            if start_row != end_row and start_col != end_col:
                return False  

            if start_row == end_row:
                direction = 1 if end_col > start_col else -1
                for col in range(start_col + direction, end_col, direction):
                    if Board.board[start_row][col] != "-":
                        return False

            if start_col == end_col:
                direction = 1 if end_row > start_row else -1
                for row in range(start_row + direction, end_row, direction):
                    if Board.board[row][start_col] != "-":
                        return False

            destination_piece = Board.board[end_row][end_col]
            if destination_piece == "-" or destination_piece[0] != piece[0]:
                return True  

        return False

    def validKnight(self, start_row, start_col, end_row, end_col, piece):
        destination_piece = self.board[end_row][end_col]
        if (abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1) or \
                (abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2):
            if destination_piece == "-" or destination_piece[0] != piece[0]:
                return True

        return False

    def validBishop(self, start_row, start_col, end_row, end_col, piece):
        if piece == "bB" or piece == "wB":
            if abs(start_row - end_row) != abs(start_col - end_col):
                return False  

            row_direction = 1 if end_row > start_row else -1
            col_direction = 1 if end_col > start_col else -1

            row = start_row + row_direction
            col = start_col + col_direction
            while row != end_row and col != end_col:
                if Board.board[row][col] != "-":
                    return False
                row += row_direction
                col += col_direction

            destination_piece = Board.board[end_row][end_col]
            if destination_piece == "-" or destination_piece[0] != piece[0]:
                return True  

        return False

    def validQueen(self, start_row, start_col, end_row, end_col, piece):
        if piece == "bQ" or piece == "wQ":
            if start_row != end_row and start_col != end_col and abs(start_row - end_row) != abs(start_col - end_col):
                return False

            if start_row == end_row:
                direction = 1 if end_col > start_col else -1
                for col in range(start_col + direction, end_col, direction):
                    if self.board[start_row][col] != "-":
                        return False

            elif start_col == end_col:
                direction = 1 if end_row > start_row else -1
                for row in range(start_row + direction, end_row, direction):
                    if self.board[row][start_col] != "-":
                        return False

            else:
                row_direction = 1 if end_row > start_row else -1
                col_direction = 1 if end_col > start_col else -1

                row = start_row + row_direction
                col = start_col + col_direction
                while row != end_row and col != end_col:
                    if self.board[row][col] != "-":
                        return False
                    row += row_direction
                    col += col_direction

            destination_piece = self.board[end_row][end_col]
            if destination_piece == "-" or destination_piece[0] != piece[0]:
                return True

        return False




    def validKing(self, start_row, start_col, end_row, end_col, piece):
        if piece == "bK" or piece == "wK":
            if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
                destination_piece = self.board[end_row][end_col]
                if destination_piece == "-" or destination_piece[0] != piece[0]:
                    return not self.in_check(start_row, start_col, end_row, end_col, piece)  

            # Check for castling
            if start_row == end_row and abs(start_col - end_col) == 2:
                if not self.in_check(start_row, start_col, start_row, (start_col + end_col) // 2, piece):  
                    if self.is_castling_allowed(start_row, start_col, end_row, end_col):
                        return True

        return False  # Invalid piece or capture

    def is_legal_move(self, start_row, start_col, end_row, end_col):
        piece = Board.board[start_row][start_col]

        if piece == "wP" or piece == "bP":
        # Prüfe, ob der Zug ein gültiger Bauerzug ist
            if Board.validPawn(start_row, start_col, end_row, end_col, piece):
            # Prüfe, ob der Zug den König im Schach setzt
                return not Board.move_puts_king_in_check(start_row, start_col, end_row, end_col, piece)

        elif piece == "wR" or piece == "bR":
        # Prüfe, ob der Zug ein gültiger Turmzug ist
            if Board.validRook(start_row, start_col, end_row, end_col, piece):
            # Prüfe, ob der Zug den König im Schach setzt
                return not Board.move_puts_king_in_check(start_row, start_col, end_row, end_col, piece)

        elif piece == "wN" or piece == "bN":
        # Prüfe, ob der Zug ein gültiger Springerzug ist
            if Board.validKnight(start_row, start_col, end_row, end_col, piece):
            # Prüfe, ob der Zug den König im Schach setzt
                return not Board.move_puts_king_in_check(start_row, start_col, end_row, end_col, piece)

        elif piece == "wB" or piece == "bB":
        # Prüfe, ob der Zug ein gültiger Läuferzug ist
            if Board.validBishop(start_row, start_col, end_row, end_col, piece):
            # Prüfe, ob der Zug den König im Schach setzt
                return not Board.move_puts_king_in_check(start_row, start_col, end_row, end_col, piece)

        elif piece == "wQ" or piece == "bQ":
        # Prüfe, ob der Zug ein gültiger Damezug ist
            if Board.validQueen(start_row, start_col, end_row, end_col, piece):
            # Prüfe, ob der Zug den König im Schach setzt
                return not Board.move_puts_king_in_check(start_row, start_col, end_row, end_col, piece)

        elif piece == "wK" or piece == "bK":
        # Prüfe, ob der Zug ein gültiger Königszug ist
            if Board.validKing(start_row, start_col, end_row, end_col, piece):
            # Prüfe, ob der Zug den König im Schach setzt
                return not Board.move_puts_king_in_check(start_row, start_col, end_row, end_col, piece)

        return False
    
    def move_puts_king_in_check(self, start_row, start_col, end_row, end_col):
    # Make a copy of the board
        board_copy = [row[:] for row in self.board]

    # Perform the move on the copied board
        piece = board_copy[start_row][start_col]
        board_copy[end_row][end_col] = piece
        board_copy[start_row][start_col] = "-"

    # Get the color of the current player
        color = piece[0]

    # Find the position of the king
        king_row, king_col = None, None
        for row in range(8):
            for col in range(8):
                if board_copy[row][col] == color + "K":
                    king_row, king_col = row, col
                    break

    # Check if the king is under attack
        opponent_color = "w" if color == "b" else "b"
        for row in range(8):
            for col in range(8):
                if board_copy[row][col][0] == opponent_color:
                    if self.valid_move(row, col, king_row, king_col, board_copy):
                        return True

        return False


def test_move_piece():
    board = Board()
    board.print_board()
    assert board.move_piece("g1f3") == True
    board.print_board()

test_move_piece()
