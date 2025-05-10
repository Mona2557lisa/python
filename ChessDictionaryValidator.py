print("name : monalisa.n \n usn : 1AY24AI073 \n section : O ")

def is_valid_chess_board(board):
    valid_pos = {f"{f}{r}" for f in 'abcdefgh' for r in '12345678'}
    valid_names = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}
    counts = {'w': 0, 'b': 0, 'wpawn': 0, 'bpawn': 0, 'wking': 0, 'bking': 0}

    for pos, piece in board.items():
        if pos not in valid_pos or piece[0] not in 'wb' or piece[1:] not in valid_names:
            return False
        counts[piece[0]] += 1
        if 'pawn' in piece:
            counts[piece] += 1
        if 'king' in piece:
            counts[piece] += 1

    return (counts['w'] <= 16 and counts['b'] <= 16 and
            counts['wpawn'] <= 8 and counts['bpawn'] <= 8 and
            counts['wking'] == 1 and counts['bking'] == 1)

# Example board
board = {
    'e1': 'wking', 'e8': 'bking',
    'a2': 'wpawn', 'b2': 'wpawn',
    'a7': 'bpawn', 'b7': 'bpawn'
}

print("Valid?" , is_valid_chess_board(board))
