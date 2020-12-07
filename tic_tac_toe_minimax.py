from tic_tac_toe_model import TicTacToeModel as model
import random

moves_cache = dict()


def get_next_move(player, model):
    if model.board_size >= 5 and model.num_moves < model.board_size * 2 - 2:
        return random.choice(list(model.remaining_moves))
    best_score = -2
    best_move = None
    for move_option in model.remaining_moves:
        model.make_move(move_option, player)
        option_score = minimax(model, player, False, -2, 2)
        model.undo_move()
        if option_score > best_score:
            best_score = option_score
            best_move = move_option
    return best_move


# TODO: Maybe take depth into account for (impossible) imperfect games
def minimax(model, our_player, maximizing, alpha, beta):
    situation_str = str(model.board) + str(our_player) + str(maximizing)
    if situation_str in moves_cache:
        return moves_cache[situation_str]

    if model.winner is not None:
        return 1 if model.winner == our_player else -1
    elif model.filled():
        return 0

    highest_score = -1
    highest_move = None
    lowest_score = 1
    lowest_move = None
    for move_option in model.remaining_moves:
        model.make_move(move_option, model.current_player)
        model.check_winner(move_option)
        option_score = minimax(model, our_player, not maximizing, alpha, beta)
        if option_score > highest_score:
            highest_score = option_score
            highest_move = move_option
        if option_score < lowest_score:
            lowest_score = option_score
            lowest_move = move_option
        model.undo_move()
        if maximizing:
            alpha = max(alpha, highest_score)
            if alpha >= beta:
                break
        else:
            beta = min(beta, lowest_score)
            if beta <= alpha:
                break

    result = highest_score if maximizing else lowest_score
    moves_cache[situation_str] = result

    return highest_score if maximizing else lowest_score
