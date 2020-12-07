import tic_tac_toe_model.TicTacToeModel as model


def get_next_move(model, player):
    best_score = -2
    best_move = None
    for move_option in model.get_remaining_moves():
        model.make_move(move_option, player)
        option_score = minimax(model, player, False)
        model.undo_last_move()
        if option_score > best_score:
            best_score = option_score
            best_move = move_option
    return best_move


# TODO: Maybe take depth into account for (impossible) imperfect games
def minimax(model, our_player, maximizing):
    if model.winner is not None:
        return 1 if model.winner == our_player else -1
    elif model.filled():
        return 0

    minimax_scores = list()
    for move_option in model.remaining_moves():
        model.make_move(move_option, model.current_player)
        model.check_winner(move_option)
        minimax_scores.append(move_option, model, our_player, not maximizing)
        model.undo_last_move()

    return max(minimax_scores) if maximizing else min(minimax_scores)
