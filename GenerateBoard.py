import sys
import numpy as np
import ipdb # ipdb.set_trace()
import csv
import pandas as pd
import os
from time import sleep

def GenerateBoard(height, width):
    """ Generates a random initial board of a specified width and height"""

    path = 'boards/randomboard.csv'
    data = pd.DataFrame(np.random.randint(1,5 ,size = (height,width)))

    if(os.path.exists(path)):

         try:
             os.remove(path)
             pd.DataFrame(data).to_csv(path, header=None, index=None, encoding='utf-8')
        # In case boards are generated too fast, the function sleeps for 50ms
         except PermissionError:
             try:
                 sleep(0.05)
                 os.remove(path)
                 pd.DataFrame(data).to_csv(path, header=None, index=None, encoding='utf-8')
             # if 50ms of sleep is not enough, sleep for an additional 500ms
             except PermissionError:
                 sleep(0.5)
                 os.remove(path)
                 pd.DataFrame(data).to_csv(path, header=None, index=None, encoding='utf-8')

    else:
        pd.DataFrame(data).to_csv(path, header=None, index=None, encoding='utf-8')

if __name__ == '__main__':
    if len(sys.argv) > 3:
        sys.exit("Usage: python GenerateBoard.py [height] [width]")
    height = int(sys.argv[1]) if len(sys.argv) > 1 else 11
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 22

    GenerateBoard(height, width)
