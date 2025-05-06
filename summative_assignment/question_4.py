class Jigsaw:
    """
    Class Jigsaw represents a jigsaw puzzle, and the operations to solve it.

    Attributes:
        _placed_pieces (dict): A dictionary that maps pieces to their position.
        _jigsaw (list): The jigsaw board represented by a 2d list
    """

    def __init__(self, rows=4, columns=4):
        """
        Initialises the jigsaw board.

        Args:
            rows (int): The number of rows in the jigsaw (default minimum 4).
            columns (int): The number of columns in the jigsaw (default minimum 4).

        Raises:
            ValueError: If rows or columns is less than 4.
        """

        if rows < 4 or columns < 4:
            raise ValueError("The board must be at least 4x4")

        self._placed_pieces = {}
        self._jigsaw = [[0 for _ in range(columns)] for _ in range(rows)]

    def add_piece(self, piece, position):
        """
        Tries to add a piece to the jigsaw board at a specific position.

        Args:
            piece (tuple of tuples): Jigsaw piece represented as a 2d tuple of ints.
            position (tuple): The (row, column) of the top left corner where the piece is to be placed.

        Returns:
            bool: True if piece was successfully placed, else False.
        """
        row_offset, col_offset = position
        piece_rows = len(piece)
        piece_cols = len(piece[0])

        for r in range(piece_rows):
            for c in range(piece_cols):
                if piece[r][c] == 0:
                    continue
                board_r = row_offset + r
                board_c = col_offset + c
                if (board_r >= len(self._jigsaw) or board_c >= len(self._jigsaw[0]) or
                        self._jigsaw[board_r][board_c] != 0):
                    return False

        for r in range(piece_rows):
            for c in range(piece_cols):
                if piece[r][c] != 0:
                    self._jigsaw[row_offset + r][col_offset + c] = piece[r][c]

        self._placed_pieces[piece] = position
        return True

    def is_solvable(self, pieces):
        """
        Finds out if the jigsaw is solvable using a subset of the given pieces.

        Args:
            pieces (set of tuples): Set of jigsaw pieces, where each is a 2d tuple of integers.

        Returns:
            bool: True is board is fully covered using some of the pieces, else False.
        """
        def _is_filled():
            """Check the board hasn't got empty cells."""
            return all(cell != 0 for row in self._jigsaw for cell in row)

        def _place_piece(p, pos):
            """Place piece (p) the jigsaw at position (pos)."""
            r0, c0 = pos
            for r in range(len(p)):
                for c in range(len(p[0])):
                    if p[r][c] != 0:
                        self._jigsaw[r0 + r][c0 + c] = p[r][c]
            self._placed_pieces[p] = pos

        def _remove_piece(p, pos):
            """Remove piece (p) from the jigsaw at position (pos)"""
            r0, c0 = pos
            for r in range(len(p)):
                for c in range(len(p[0])):
                    if p[r][c] != 0:
                        self._jigsaw[r0 + r][c0 + c] = 0
            self._placed_pieces.pop(p, None)

        def _can_place(p, r0, c0):
            """Check piece (p) can be placed with no overlap or out of bounds."""
            for r in range(len(p)):
                for c in range(len(p[0])):
                    if p[r][c] == 0:
                        continue
                    if (r0 + r >= len(self._jigsaw) or c0 + c >= len(self._jigsaw[0]) or
                            self._jigsaw[r0 + r][c0 + c] != 0):
                        return False
            return True

        def _backtrack(remaining):
            """Recursive backtracking that attempts to place the remaining pieces"""
            if _is_filled():
                return True
            for i, p in enumerate(remaining):
                for r in range(len(self._jigsaw)):
                    for c in range(len(self._jigsaw[0])):
                        if _can_place(p, r, c):
                            _place_piece(p, (r, c))
                            if _backtrack(remaining[:i] + remaining[i + 1:]):
                                return True
                            _remove_piece(p, (r, c))
            return False

        return _backtrack(list(pieces))