def compute_code(board):
    if len(board) != 9 or board.count(0) != 3 or board.count(1) != 3 or board.count(2) != 3:
        return None
    else:
        result = 0
        for i, num in enumerate(board):
            result += num * (3 ** i)
        return result
