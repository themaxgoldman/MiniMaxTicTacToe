from tic_tac_toe_model import TicTacToeModel
import random

moves_cache = dict()


def get_next_move(player, model):
    if model.board_size >= 5 and len(model) < model.board_size * 2 - 3:
        return random.choice(list(model.remaining_moves))
    highest_score = -2
    highest_move = None
    for move_option in model.remaining_moves:
        model.make_move(move_option, player)
        option_score = minimax(model, player, False, alpha=-2, beta=2)
        model.undo_move()
        if option_score > highest_score:
            highest_score = option_score
            highest_move = move_option
    return highest_move


def minimax(model, our_player, maximizing, alpha, beta):
    situation_str = str(model.board) + str(our_player) + \
        str(maximizing) + str(alpha) + str(beta)
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
            alpha = max(highest_score, alpha)
            if beta <= alpha:
                break
        else:
            beta = min(lowest_score, beta)
            if(beta <= alpha):
                break

    result = highest_score if maximizing else lowest_score
    moves_cache[situation_str] = result

    return result
