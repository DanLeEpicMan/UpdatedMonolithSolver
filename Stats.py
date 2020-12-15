import sys
import numpy as np
from numpy import genfromtxt
import ipdb # ipdb.set_trace()
import csv
from THM import Heuristics, Cost, Node, StackFrontier, QueueFrontier, AStarFrontier, maxleft, maxright, maxup, maxdown, neighbors, Exhaustive_coordinates, Adjacent, Clickable, Click, Solve, THM
from GenerateBoard import GenerateBoard

def Stats(height, width, max_states, samples):
    """ Return the mean, standard deviation, coefficient of variance, min and max of the following parameters: percentage of board cleared, number of states explored, number of steps for the best solution, boolean of whether max states were exceeded. The parameters are computed for a given amount of samples for a board with a given height and width and given a max amount of states to search"""

    arr_cleared = []
    arr_num_explored = []
    arr_steps = []
    arr_max_exceeded = []

    for i in range(0, samples):
        GenerateBoard(height, width)

        solution, states, num_explored, cleared, max_exceeded = THM('randomboard', 100, max_states, 0)

        cleared = round(cleared, 2)

        arr_cleared.append(cleared)
        arr_num_explored.append(num_explored)
        if solution is not None:
            arr_steps.append(len(solution))
        else:
            arr_steps.append(0)
        arr_max_exceeded.append(max_exceeded)

    cleared_mean = round(np.mean(arr_cleared), 3)
    cleared_std = round(np.std(arr_cleared), 3)
    cleared_cov = cleared_std / cleared_mean
    cleared_min = np.min(arr_cleared)
    cleared_max = np.max(arr_cleared)

    num_explored_mean = round(np.mean(arr_num_explored), 3)
    num_explored_std = round(np.std(arr_num_explored), 3)
    num_explored_cov = num_explored_std / num_explored_mean
    num_explored_min = np.min(arr_num_explored)
    num_explored_max = np.max(arr_num_explored)

    steps_mean = round(np.mean(arr_steps), 3)
    steps_std = round(np.std(arr_steps), 3)
    steps_cov = steps_std / steps_mean
    steps_min = np.min(arr_steps)
    steps_max = np.max(arr_steps)

    max_exceeded_mean = round(np.mean(arr_max_exceeded), 3)
    max_exceeded_std = round(np.std(arr_max_exceeded), 3)
    max_exceeded_cov = max_exceeded_std / max_exceeded_mean
    max_exceeded_min = np.min(arr_max_exceeded)
    max_exceeded_max = np.max(arr_max_exceeded)

    print("\n__Cleared__\n")
    print(f"Mean: {cleared_mean}")
    print(f"STD: {cleared_std}")
    print(f"COV: {cleared_cov}")
    print(f"Min: {cleared_min}")
    print(f"Max: {cleared_max}")

    print("\n__Num_Explored__\n")
    print(f"Mean: {num_explored_mean}")
    print(f"STD: {num_explored_std}")
    print(f"COV: {num_explored_cov}")
    print(f"Min: {num_explored_min}")
    print(f"Max: {num_explored_max}")

    print("\n__Steps__\n")
    print(f"Mean: {steps_mean}")
    print(f"STD: {steps_std}")
    print(f"COV: {steps_cov}")
    print(f"Min: {steps_min}")
    print(f"Max: {steps_max}")

    print("\n__Max_Exceeded__\n")
    print(f"Mean: {max_exceeded_mean}")
    print(f"STD: {max_exceeded_std}")
    print(f"COV: {max_exceeded_cov}")
    print(f"Min: {max_exceeded_min}")
    print(f"Max: {max_exceeded_max}")

if __name__ == "__main__":

    if len(sys.argv) > 5:
        sys.exit("Usage: python Stats.py [height] [width] [maximum board state searches] [samples]")
    height = int(sys.argv[1]) if len(sys.argv) > 1 else sys.exit("Usage: python Stats.py [height] [width] [maximum board state searches] [samples]")
    width = int(sys.argv[2]) if len(sys.argv) > 2 else sys.exit("Usage: python Stats.py [height] [width] [maximum board state searches] [samples]")
    max_states = int(sys.argv[3]) if len(sys.argv) > 3 else 2000
    samples = int(sys.argv[4]) if len(sys.argv) > 4 else 10

    m = Stats(height, width, max_states, samples)
