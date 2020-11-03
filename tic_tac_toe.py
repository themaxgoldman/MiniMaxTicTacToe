from tic_tac_toe_model import TicTacToeModel


def player_mark(player):
    if player == 1:
        return "O"
    elif player == 0:
        return "X"
    else:
        return " "


def display_board(board):
    """
    |---|---|---|
    | O |   | X |
    |---|---|---|
    | X |   | O |
    |---|---|---|
    |   |   | X |
    |---|---|---|
    """
    size = len(board)
    divider = "|---" * size + "|"
    print()
    for x in range(size):
        row = "|"
        for y in range(size):
            row += " " + player_mark(board[x][y]) + " |"
        print(divider)
        print(row)
    print(divider)


def get_next_move(player):
    raw_move = input(
        "Enter move (x,y) player {player}: ".format(player=player))
    xy = raw_move.split(",")
    x = xy[0][len(xy[0]) - 1]
    y = xy[1][0]
    return (int(x), int(y))


def main():
    print("-- Tic Tac Toe --\n")
    model = TicTacToeModel()
    while True:
        display_board(model.board)
        current_player = model.current_player
        (x, y) = get_next_move(current_player)
        model.make_move(x, y, current_player)
        if model.check_winner(x, y):
            display_board(model.board)
            print("Player {player} won!".format(player=current_player))
            break
        if model.filled():
            display_board(model.board)
            print("Game over: Tie!")
            break


if __name__ == "__main__":
    main()
