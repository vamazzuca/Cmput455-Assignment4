#!/usr/bin/python3
# /usr/bin/python3
# Set the path to your python3 above

from gtp_connection import GtpConnection
from board_util import GoBoardUtil
from board import GoBoard
#################################################
class Random:
    def __init__(self):
        """
        NoGo player that selects moves randomly from the set of legal moves.

        Parameters
        ----------
        name : str
            name of the player (used by the GTP interface).
        version : float
            version number (used by the GTP interface).
        """

        self.name = "Random"
        self.version = 1.0

    def get_move(self, board:GoBoard, color:int):
        """
        Select a random move.
        """
        move = GoBoardUtil.generate_random_move(board, color)
        return move
        
def run():
    """
    start the gtp connection and wait for commands.
    """
    board = GoBoard(7)
    con = GtpConnection(Random(), board)
    con.start_connection()

if __name__ == "__main__":
    run()
