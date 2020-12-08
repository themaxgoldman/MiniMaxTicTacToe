from tic_tac_toe_model import TicTacToeModel
from flask import Flask, redirect, request
from tic_tac_toe_minimax import get_next_move
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return redirect('/move')


@app.route('/move', methods=['POST'])
def move():
    board_size = int(request.form.get('board_size'))
    player = int(request.form.get('player'))
    num_moves = int(request.form.get('num_moves'))
    board = [[None for x in range(board_size)]
             for y in range(board_size)]
    remaining_moves = {(x, y)
                       for x in range(board_size)
                       for y in range(board_size)}
    for x in range(board_size):
        for y in range(board_size):
            spot = request.form.get(str((x, y)), None)
            if spot is not None:
                board[x][y] = int(spot)
                remaining_moves.remove((x, y))

    model = TicTacToeModel(board_size)
    model.current_player = player
    model.num_moves = num_moves
    model.board = board
    model.remaining_moves = remaining_moves

    response = str(get_next_move(player, model))
    print(model)
    print(response)
    return response


if __name__ == "__main__":
    app.run(port=5000, debug=True)
