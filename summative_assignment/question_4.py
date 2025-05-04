class Jigsaw:
    def __init__(self, rows=4, columns=4):
        if rows < 4 or columns < 4:
            raise ValueError("Columns and rows must both be 4.")
        self._jigsaw = [[0 for _ in range(columns)] for _ in range(rows)]
        self._placed_pieces = {}

    def add_piece(self, piece, pos):
        rows = len(self._jigsaw)
        cols = len(self._jigsaw[0])
        piece_rows = len(piece)
        piece_cols = len(piece[0])
        row_offset, cols_offset = pos

        if row_offset + piece_rows > rows or cols_offset + piece_cols > cols:
            return False

        for r in range(piece_rows):
            for c in range(piece_cols):
                value = piece[r][c]
                if value == 0:
                    continue
                r_board = row_offset + r
                c_board = cols_offset + c
                if self._jigsaw[r_board][c_board] != 0:
                    return False

        for r in range(piece_rows):
            for c in range(piece_cols):
                value = piece[r][c]
                if value != 0:
                    self._jigsaw[row_offset + r][cols_offset + c] = value

        self._placed_pieces[piece] = pos
        return True


    def is_solvable(self):
        pass

# TODO: is_solvable method, add value error messages, code documentation, edit for efficiency