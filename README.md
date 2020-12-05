# MinimaxTicTacToe
Arbitrarily large tic tac toe against Minimax AI
## Milestone 1
### Description
Minimax TicTacToe will utilize a client/server architecture to run an arbitrarily large tic tac toe game against an AI. The purpose of the server is to cache responses to the human player's moves independent of the current game. This is useful because the Minimax algorithm will dramatically decrease in speed as the size of the board increases. The client will display the game, prompt the user for moves, show the AI's moves, maintain a game state, and handle communication with the flask server in the background. The server will simply run the Minimax algorithm on the state it is given and send back a move by the AI. It will cache this decision based on the given state to improve speed down the line.

### Dependencies
The project will use `unittest` to test the tic tac toe model functionality. It may be used to test the Minimax algorithm, I'm not sure how this could work yet. `Flask` will be used to host the server and `requests` will be used by the client to communicate with the server. I will likely use `numpy` to try to improve some of the calculations the game model does such as checking for a winner. I also anticipate that `numpy` could be useful for some operations in the Minimax algorithm. 