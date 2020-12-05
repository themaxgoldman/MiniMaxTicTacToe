import tic_tac_toe_model as model
from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'Flask app for TicTacToe!'


@app.route('/get_move')
def get_move():
    return 'Need To Implement Make Move!'


if __name__ == '__main__':
    main(sys.argv)
