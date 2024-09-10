def is_valid_move(board, row, col, seen):
    n = board[row][col]
    for i in range(9):
        number = board[row][i]
        if i != col and number in seen['row'][row]:
            __import__('pdb').set_trace()
            return False
        if number != ".":
            seen['row'][row].add(number)

        number = board[i][col]
        if i != row and number in seen['col'][col]:
            __import__('pdb').set_trace()
            return False
        if number != ".":
            seen['col'][col].add(number)
    return True

def is_valid(board, row=0, col=0, seen=None):
    if not seen:
        row_seen = [set() for i in range(9)]
        col_seen = [set() for i in range(9)]
        seen = {'row': row_seen, 'col': col_seen}
    if row == 9:
        return True
    if col == 9:
        return is_valid(board, row+1, 0, seen)
    if board[row][col] == ".":
        return is_valid(board, row, col+1, seen)
    if is_valid_move(board, row, col, seen):
        is_valid(board, row, col+1, seen)
    __import__('pdb').set_trace()
    return False
