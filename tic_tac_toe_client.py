from tic_tac_toe_model import TicTacToeModel
import sys
import requests
import tic_tac_toe_minimax as minimax

server_endpoint = 'http://127.0.0.1:5000/move'


def player_mark(player):
    if player == 1:
        return "O"
    elif player == 0:
        return "X"
    else:
        return " "


def get_next_move_from_server(player, model):
    payload = dict()
    payload['board_size'] = model.board_size
    payload['player'] = player
    payload['num_moves'] = model.num_moves
    for x in range(model.board_size):
        for y in range(model.board_size):
            if model.board[x][y] is not None:
                payload[str((x, y))] = model.board[x][y]

    r = requests.post(server_endpoint, data=payload)
    print(r.text)
    raw_move = r.text
    xy = raw_move.split(", ")
    x = xy[0][len(xy[0]) - 1]
    y = xy[1][0]
    return (int(x), int(y))


def get_next_move(player, model):
    # TODO: Convert to single player with one AI
    if player == 1:
        return get_next_move_from_server(player, model)
    raw_move = input(
        "Enter move (x,y) player {player}: ".format(player=player))
    xy = raw_move.split(",")
    x = xy[0][len(xy[0]) - 1]
    y = xy[1][0]
    return (int(x), int(y))


def main():
    # TODO: Convert to single player with one AI
    print("-- Tic Tac Toe --\n")
    model = TicTacToeModel()
    if len(sys.argv) > 1:
        model = TicTacToeModel(int(sys.argv[1]))
    while True:
        print(model)
        current_player = model.current_player
        next_move = get_next_move(current_player, model)
        try:
            model.make_move(next_move, current_player)
        except ValueError as err:
            print(err)
            print("Try again!")
            continue
        if model.check_winner(next_move):
            print(model)
            print("Player {player} won!".format(player=current_player))
            break
        if model.filled():
            print(model)
            print("Game over: Tie!")
            break


if __name__ == "__main__":
    main()
