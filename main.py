import os
import chess
import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers
from chessboard import display

board = chess.Board()

while True:
    display.start(board.fen())