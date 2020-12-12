from tic_tac_toe_model import TicTacToeModel
import sys
import requests
import tic_tac_toe_minimax as minimax
import argparse

server_endpoint = 'http://127.0.0.1:5000/move'


def get_next_move_from_server(player, model):
    """ Retrieves the next move from the 
        ai server

    Args:
        player (int): the current player
        model (TicTacToeModel): the model to send and evaluate

    Returns:
        (int, int): the resultant move
    """
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


def get_next_move(player, model, ai):
    """ Get the next move from either a
        human player or the ai

    Args:
        player (int): the current player
        model (TicTacToeModel): the model to get move for
        ai (int): the player that is the ai

    Returns:
        (int,int): the next move to make
    """
    if player == ai:
        return get_next_move_from_server(player, model)
    raw_move = input(
        "Enter move (x,y) player {player}: ".format(player=player))
    xy = raw_move.split(",")
    x = xy[0][len(xy[0]) - 1]
    y = xy[1][0]
    return (int(x), int(y))


def main():
    print("-- Tic Tac Toe --\n")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--size", help="size of the one side of the board", type=int)
    parser.add_argument(
        "--ai", help="which player for ai, -1 for no ai", type=int, default=1)
    args = parser.parse_args()
    ai = args.ai
    size = args.size
    model = None
    if size:
        model = TicTacToeModel(size)
    else:
        model = TicTacToeModel()
    while True:
        print(model)
        current_player = model.current_player
        next_move = get_next_move(current_player, model, ai)
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
