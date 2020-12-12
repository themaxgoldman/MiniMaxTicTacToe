# MinimaxTicTacToe
Arbitrarily large tic tac toe against a minimax AI

## Description

### Overview
Minimax TicTacToe is a standard tic tac toe game that utilizes a inimax algorithm to power its AI. The AI will always choose the optimal move, leading to either a win (if the human player messes up) or a tie. It will never lose. The demo is located [here](https://minimaxgames.s3.amazonaws.com/project_demo.mp4).

### Server/AI
* `tic_tac_toe_server.py
* `tic_tac_toe_minimax.py`

The minimax AI is run on a `Flask` server that utilizes two main optimizations to significantly speed up its computations. 

[*alpha/beta pruning*](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) -  stops the computations on a decision tree once a higher up on the decision tree has been proven to be worse than a preciously calculated decision

*decision caching* - decisions are cached in a `dictionary` and if the result of a previous decision is needed it is retrieved from the cache instead of recalculated

Additionally, the server itself is an optimization in the long run. Because of the caching, the server gets faster with more requests over time. The server allows the cache to persist throughout multiple game runs independent of the client

### Client
* `tic_tac_toe_client.py`

The client is relatively straightforward. The `main` gets the specified arguments using `argparse` and then begins a standard game loop. There are two functions for the `main` to retrieve moves. `get_next_move` determines whether the current player is the AI or the human player and either retrieves the human input or calls `get_next_move_from_server`. `get_next_move_from_server` builds a payload using information from the model and sends it to the server as form data in a `POST` request using `requests`

### Model
* `tic_tac_toe_model.py`

The project has a fully fleshed out tic tac model. There's not much to it, after all it's tic tac toe. However, there are a few notable features. Moves are kept maintained in a `list` treated as a stack so that moves can be undone by minimax to increase speed. I was originally using the `copy` function in minimax to pass the board state down however this was extremely inefficient as a deep copy of the board was needed. Also, `check_winner` only checks the rows, columns, and diagonals of a given spot in order to increase efficiency. Finally, a `set` of remaining moves is maintained in order to speed up the minimax algorithm which needs to retrieve this set frequently

### Testing
* `test_tic_tac_toe_model.py`

There are lots of unit tests written using the `unittest` library in `test_tic_tac_toe_model.py`. These tests turned out to be very useful not only when I first wrote the model, but also when I was making optimizations as I could see whether or not my changes had broken the game model.


## Installation/Running Instructions
The project has the following dependencies, for convenience I also included them in a `requirements.txt` file.

* `requests`
* `argparse`
* `unittest`
* `Flask`

First, the server file should be run - `tic_tac_toe_server.py`. Then the client should be run - `tic_tac_toe_client.py`. The client has optional parameters `--size` and `--ai`. `--size` indicates the board size and `--ai` indicates which player (if any) should be AI. Both have help text. You also may need to change the server endpoint in the client file. Additionally, the unit tests can be run in `test_tic_tac_toe_model.py`.


## Thank you!
Thank you for a great semester, I really enjoyed this class and enjoyed learning python. I especially had fun with this project and hope you find it to be interesting as well.
