import os, shutil
from os import path
import sys
import time
import csv
import numpy as np
from numpy import genfromtxt
import subprocess

def Cleared(state, height, width):
    """Determines the percentage of a given board that has been cleared"""
    total_fields = height * width
    noncleared_fields = np.count_nonzero(state)
    cleared_fields = total_fields - noncleared_fields

    H = (cleared_fields / total_fields) * 100

    return H


def Heuristics(state, height, width, exhaustive_coords):
    """The Heuristics of a state are given as a sum of the cleared and apparent clearable nodes in the state"""
    H1 = np.sum(Clearable(state, height, width, exhaustive_coords))
    H2 = height * width - np.count_nonzero(state)

    H = H1 + H2

    return H

def Cost(depth):
    """The cost has been defined as the depth (positive) to slightly favor solutions with more steps as it is likely that these will clear more of the board """

    G = depth
    return G

class Node():
    def __init__(self, state, depth, parent, action, cleared, value):
        self.state = state
        self.depth = depth
        self.parent = parent
        self.action = action
        self.cleared = cleared
        self.value = value

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        """Returns True if the frontier contains a node which contains a given state"""
        return any(np.all(node.state == state) for node in self.frontier)

    def empty(self):
        """Returns True if the frontier contains no nodes"""
        return len(self.frontier) == 0

    def remove(self):
        """Pops the node that was most recently added to the frontier"""
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        """Pops the first node of the frontier"""
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class AStarFrontier(StackFrontier):

    def remove(self):
        """Pops the node with the highest value as defined by H + G"""

        if self.empty():
            raise Exception("empty frontier")
        else:
            values = []
            for nodes in self.frontier:
                values.append(nodes.value)
            index_max = np.argmax(values)
            node = self.frontier.pop(index_max)
            return node

def maxleft(action):
    """Returns how many positions are to the left of an action in a given state"""
    max_left = action[1]
    return max_left

def maxright(action, width):
    """Returns how many positions are to the right of an action in a given state"""
    max_right = width - action[1] - 1
    return max_right

def maxup(action):
    """Returns how many positions are above an action in a given state"""
    max_up = action[0]
    return max_up

def maxdown(action, height):
    """Returns how many positions are below an action in a given state"""
    max_down = height - action[0] - 1
    return max_down

def neighbors(action, height, width):
    """Returns possible neighboring actions for a given action in a state"""
    actions = []
    if maxleft(action) != 0:
        actions.append((action[0], action[1]-1))
    if maxright(action, width) != 0:
        actions.append((action[0], action[1]+1))
    if maxup(action) != 0:
        actions.append((action[0]-1, action[1]))
    if maxdown(action, height) != 0:
        actions.append((action[0]+1, action[1]))
    return actions

def Exhaustive_coordinates(height, width):
    """Returns an exhaustive list of coordinates for a state of a given size"""

    actions = []
    for i in range(0, height):
        for j in range(0, width):
            coord = (i, j)
            actions.append(coord)
    return actions

def Adjacent(state, action, height, width):
    """Returns a boolean matrix that describes if values in a state are both adjacent and identical to the value of a given action"""

    # preallocating the boolean array and adding the starting action as True
    A = np.zeros((height, width))
    A[action] = 1

    # define the start node and initial actions. the state is given as the first action (point)
    start = Node(state=A, depth=None, parent=None, action=action, cleared=None, value=None)
    value = state[action]
    # frontier is given as a stack frontier, using depth first search as the search is exhaustive
    frontier = StackFrontier()
    frontier.add(start)

    # Initialize an empty explored set
    explored = []

    while True:

        # If nothing is left in frontier, then adjacency check is complete
        if frontier.empty():
            return A

        # Choose a node from the frontier
        node = frontier.remove()

        # Mark node as explored
        explored.append(node.action)
        # Add neighboring actions to frontier and check if adjacent actions have identical values
        for action in neighbors(node.action, height, width):
            if action not in explored and state[action] == value:
                A = node.state
                A[action] = 1
                child = Node(state=A,depth=None,parent=node, action=action, cleared=None,value=None)
                frontier.add(child)


def Clickable(state, height, width, exhaustive_coords):
    """Returns a boolean matrix for which the indices describe the possible actions of a given board state"""

    # Preallocating the boolean array for the 'Clickable' function
    C = np.zeros((height, width))
    # Initialize a set of possible actions left to explore
    not_explored = exhaustive_coords.copy()

    while True:

        # If nothing is left in frontier, then clickable check is complete
        if len(not_explored) == 0:
            return C

        # Choose an action from the exhaustive list of possible actions
        action = not_explored[0]
        # unless the action is already cleared (0) then check for adjacency
        if state[action] != 0:
            A = Adjacent(state, action, height, width)

            # create a list of the actions (coordinates) corresponding to the boolean array, A
            coords = np.where(A)
            list_of_coords = list(zip(coords[0], coords[1]))

            # remove all of the actions from the list of non-explored actions
            for action in list_of_coords:
                if action in not_explored:
                    not_explored.remove(action)
            if np.sum(A) > 1:
                # add the first coordinate of the list as an action in the boolean array. Only the first coordinate is added, as taking any action in the list would result in the exact same state.
                C[list_of_coords[0]] = 1
        else:
            # if the action is cleared (0) then remove it from the list of non-explored actions
            not_explored.remove(action)

def Clearable(state, height, width, exhaustive_coords):
    """Returns a boolean matrix, for which the indices describe which actions in the state are possible to clear"""

    # Preallocating the boolean array for the 'Clearable' function
    C = np.zeros((height, width))
    # Initialize a set of possible actions left to explore
    not_explored = exhaustive_coords.copy()

    while True:

        # If nothing is left in frontier, then clearable check is complete
        if len(not_explored) == 0:
            return C

        # Choose a node from the frontier
        action = not_explored[0]

        # unless the action is already cleared (0) then check for adjacency
        if state[action] != 0:
            A = Adjacent(state, action, height, width)

            # create a list of the actions (coordinates) corresponding to the boolean array, A
            coords = np.where(A)
            list_of_coords = list(zip(coords[0], coords[1]))

            # remove all of the actions from the list of non-explored actions
            for action in list_of_coords:
                if action in not_explored:
                    not_explored.remove(action)
                if np.sum(A) > 1:
                    # every action in the list is added to the boolean array
                    C[action] = 1
        else:
            # if the action is cleared (0) then remove it from the list of non-explored actions
            not_explored.remove(action)

def Click(state, action, height, width):
    """Takes a state and an action and returns a new state, clearing the actions for which A(state, action) is True, and adding 1 to the actions where Surround(state, action) is True and not 0 (resetting at 4)"""

    def Surround(state, action, height, width):
        """ Returns a boolean matrix, for which the indices describe if the actions are neighboring to the boolean matrix A(state, action)"""
        A = Adjacent(state, action, height, width)
        S = np.zeros((height, width))

        for i in range(0, height):
            for j in range(0, width):
                # Up
                if maxup((i, j)) != 0:
                    if A[i, j] == 1 and A[i-1, j] != 1:
                        S[i-1, j] = 1
                # Right
                if maxright((i, j), width) != 0:
                    if A[i, j] == 1 and A[i, j+1] != 1:
                        S[i, j+1] = 1
                # Down
                if maxdown((i, j), height) != 0:
                    if A[i, j] == 1 and A[i+1, j] != 1:
                        S[i+1, j] = 1
                # Left
                if maxleft((i, j)) != 0:
                    if A[i, j] == 1 and A[i, j-1] != 1:
                        S[i, j-1] = 1
        return S

    C = np.copy(state)
    S = Surround(state, action, height, width)
    A = Adjacent(state, action, height, width)
    if np.sum(A) > 1:
        for i in range(0, height):
            for j in range(0, width):
                if S[i, j] == 1 and state[action] != 0:
                    if C[i, j] == 4:
                        C[i, j] = 1
                    elif C[i, j] == 0:
                        pass
                    else:
                        C[i, j] = C[i, j] + 1
                if state[i, j] > 0 and A[i, j] == 1:
                    C[i, j] = 0
    return C

def Solve(state, target, height, width, exhaustive_coords, max_states, print_output):
    """Returns a solution for a given board state with a desired clear rate, if any is available within a given amount of state searches.
    The function returns a list of actions, states, the total states explored to arrive at the solution, the clearance rate and a boolean that indicates whether the max states were exceeded"""

    start_time = time.time()

    # Initialize frontier to just the starting position
    start = Node(state=state, depth=0, parent=None, action=None, cleared=Cleared(state, height, width), value=0)
    frontier = AStarFrontier()
    frontier.add(start)

    # Initialize an empty explored set
    explored = []
    num_explored = 0
    # Initializing the best solution
    best_clear = 0
    best_depth = np.inf
    best_solution = None

    print("\nPress 'CTRL+C' to break loop early and print the current best solution")

    # Keep looping until solution is found, 'Ctrl+C' is pressed, no searches are left, or max states are exceeded
    while True:
        try:
            # If nothing is left in frontier or max states were exceeded without reaching the target clearance rate, then return best solution found
            if frontier.empty() or num_explored >= max_states:
                # if there were no possible actions, return no solution:
                if not np.sum(Clickable(start.state, height, width, exhaustive_coords)):
                    state = start.state
                    solution = None
                    num_explored = 1
                    best_clear = 0
                    max_exceeded = 0
                    return solution, state, num_explored, best_clear, max_exceeded
                else:
                    # else return the best solution that was found within the max amount of states searched
                    node = best_solution
                    state = []
                    actions = []
                    solution = []
                    while node.parent is not None:
                        state.append(node.state)
                        actions.append(node.action)
                        node = node.parent
                    # adding the initial state
                    state.append(start.state)
                    # reversing the list of states and actions
                    state.reverse()
                    actions.reverse()
                    steps = len(actions)
                    for i in range(steps):
                        solution.append(actions[i])
                    if num_explored >= max_states:
                        max_exceeded = 1
                    else:
                        max_exceeded = 0
                    return solution, state, num_explored, best_clear, max_exceeded

            # Choose a node from the frontier
            node = frontier.remove()

            # If node is the goal, then we have a solution
            if node.cleared >= target:
                state = []
                actions = []
                solution = []
                cleared = node.cleared
                max_exceeded = 0
                while node.parent is not None:
                    state.append(node.state)
                    actions.append(node.action)
                    node = node.parent
                # adding the initial state
                state.append(start.state)
                # reversing the list of states and actions
                state.reverse()
                actions.reverse()
                steps = len(actions)
                for i in range(steps):
                    solution.append(actions[i])
                return solution, state, num_explored, cleared, max_exceeded
            # Mark node as explored
            explored.append(node.state)

            # check for available actions
            C = Clickable(node.state, height, width, exhaustive_coords)

            # convert the boolean matrix into a list of actions
            coords = np.where(C)
            list_of_actions = list(zip(coords[0], coords[1]))
            for action in list_of_actions:
                state = Click(node.state, action, height, width)
                # if the frontier does not already contain the state, and it has not been explored previously, then add it to the frontier
                if not frontier.contains_state(state) and not any(np.all(state==explored,axis=(1,2))):
                    # each action in the list is assigned a value
                    H = Heuristics(state, height, width, exhaustive_coords)
                    G = Cost(node.depth)
                    value = H + G

                    child = Node(state=state, depth=node.depth+1, parent=node, action=action, cleared=Cleared(state, height, width), value=value)
                    frontier.add(child)

                    num_explored += 1
                    # if the solution is better than the previously best solution, it is saved as a node
                    if child.cleared > best_clear:
                        best_clear = child.cleared
                        best_depth = child.depth
                        best_solution = child
                    elif child.cleared == best_clear:
                        if child.depth < best_depth:
                            best_clear = child.cleared
                            best_depth = child.depth
                            best_solution = child

                    # report progress
                    if max_states > 1000 and print_output:
                        if num_explored % 1000 == 0:
                            end_time = time.time()
                            hours, rem = divmod(end_time-start_time, 3600)
                            minutes, seconds = divmod(rem, 60)
                            best_clear_print = round(best_solution.cleared, 2)
                            print("{} board states explored in {:0>2} hours, {:0>2} minutes, and {:05.2f} seconds. Current best clear rate: {} %.".format(num_explored,int(hours),int(minutes),seconds,best_clear_print))
        # break loop using 'Ctrl+C'
        except KeyboardInterrupt:
            node = best_solution
            state = []
            actions = []
            solution = []
            while node.parent is not None:
                state.append(node.state)
                actions.append(node.action)
                node = node.parent
            # adding the initial state
            state.append(start.state)
            # reversing the list of states and actions
            state.reverse()
            actions.reverse()
            steps = len(actions)
            for i in range(steps):
                solution.append(actions[i])
            if num_explored >= max_states:
                max_exceeded = 1
            else:
                max_exceeded = 0
            return solution, state, num_explored, best_clear, max_exceeded

def output_image(solution, states, height, width):
    from PIL import Image, ImageDraw

    if not os.path.exists('solutions'):
        os.mkdir('solutions')

    # clear previously printed solutions
    for filename in os.listdir('solutions'):
        file_path = os.path.join('solutions', filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    sprite = Image.open('sprites/1.png')
    cell_size, cell_size = sprite.size
    highlight_color = (197, 190, 0)
    highlight_color2 = (199, 138, 14)

    # Create a blank canvas
    img = Image.new(
        "RGBA",
        (width * cell_size, height * cell_size),
        "black"
    )
    for step in range(0, len(solution)+1):

        draw = ImageDraw.Draw(img)

        for i in range(0, height):
            for j in range(0, width):

                if states[step][i][j] == 1:
                    sprite = Image.open('sprites/1.png')
                elif states[step][i][j] == 2:
                    sprite = Image.open('sprites/2.png')
                elif states[step][i][j] == 3:
                    sprite = Image.open('sprites/3.png')
                elif states[step][i][j] == 4:
                    sprite = Image.open('sprites/4.png')
                elif states[step][i][j] == 0:
                    sprite = Image.open('sprites/0.png')

                # Draw cell
                img.paste(sprite, (cell_size*j, cell_size*i))

        # highlighting action

        if step != len(solution):
            draw.rectangle(
                    ([(solution[step][1] * cell_size, solution[step][0] * cell_size),
                      ((solution[step][1] + 1) * cell_size, (solution[step][0] + 1) * cell_size)]),
                    fill=None, outline=highlight_color2, width = 4
                )

            draw.rectangle(
                    ([(solution[step][1] * cell_size, solution[step][0] * cell_size),
                      ((solution[step][1] + 1) * cell_size, (solution[step][0] + 1) * cell_size)]),
                    fill=None, outline=highlight_color, width = 3
                )

            draw.rectangle(
                    ([(solution[step][1] * cell_size, solution[step][0] * cell_size),
                      ((solution[step][1] + 1) * cell_size, (solution[step][0] + 1) * cell_size)]),
                    fill=None, outline=highlight_color2, width = 1
                )

        img.save("solutions/step{}.png".format(str(step)))

def THM(filename, target, max_states, print_output):
    """Initalizes the Treasure Hunter Monolith solver and prints the best solution found"""

    # read file contents and import as a matrix
    try:
        state = genfromtxt("boards/"+filename+".csv", delimiter=',')
    except ValueError:
        sys.exit("Please verify that the board in"+filename+".csv is square.")

    # file contents error detection
    if np.max(state) > 4:
        sys.exit("Please verify that 'boards/"+filename+".csv' only contains values between 0 and 4.")
    elif np.min(state) < 0:
        sys.exit("Please verify that 'boards/"+filename+".csv' only contains values between 0 and 4.")
    elif np.isnan(state).any():
        sys.exit("Please verify that 'boards/"+filename+".csv' only contains values between 0 and 4.")

    # Determine height and width of board
    try:
        height = len(state)
    except TypeError:
        height = 1
    try:
        width = max(len(line) for line in state)
    except TypeError:
        width = 1

    # generate an exhaustive list of coordinates to avoid repetition
    exhaustive_coords = Exhaustive_coordinates(height, width)

    # calling the solver
    solution, states, num_explored, cleared, max_exceeded = Solve(state, target, height, width, exhaustive_coords, max_states, print_output)

    # clearing progress report
    os.system( 'cls' )

    # Printing the solution
    if print_output == 1:
        if solution is not None:
            cleared = round(cleared, 2)
            print("The best solution cleared "+str(cleared)+"% of the board and was determined by exploring "+str(num_explored)+" states, using "+str(len(solution))+" steps to be:\n "+str(solution))

            for state in states:
                print("\n"+state)

            if max_exceeded == 0:
                print("\n max states were not exceeded.")
            else:
                print("\n max states were exceeded")
        else:
            print("No solution was found")
    elif print_output == 2:
        cleared = round(cleared, 2)
        print("The best solution cleared "+str(cleared)+"% of the board and was determined by exploring "+str(num_explored)+" states, using "+str(len(solution))+" steps to be:\n "+str(solution))
        print("\nPrinting solution...")
        output_image(solution, states, height, width)
        print("\nThe best determined solution can be found in the 'solutions' folder")
        subprocess.Popen('explorer /select,' + os.path.join("solutions", "step0.png")) # Opens solutions folder w/ item selected.
    else:
        pass

    return solution, states, num_explored, cleared, max_exceeded

if __name__ == '__main__':

    # input error detection
    if len(sys.argv) > 5:
        sys.exit("Usage: python THM.py [filename] [target clearance rate in %] [maximum board state searches] [print_output]")

    if len(sys.argv) > 2:
        try:
            int(sys.argv[2])
        except:
            sys.exit("Target clearance rate must be a positive integer.")

    if len(sys.argv) > 3:
        try:
            int(sys.argv[3])
        except:
            sys.exit("Max search states must be a positive integer.")

    if len(sys.argv) > 4:
        try:
            int(sys.argv[4])
        except:
            sys.exit("Print output must be 0, 1 or 2.")

    # variable argument default values
    filename = sys.argv[1] if len(sys.argv) > 1 else "board4"
    target = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    max_states = int(sys.argv[3]) if len(sys.argv) > 3 else 5000
    print_output = int(sys.argv[4]) if len(sys.argv) > 4 else 2

    if target > 100:
        target = 100
        print("Target clearance rate has been set to 100 %.")
    elif target < 0:
        sys.exit("Target clearance rate must be between 0 and 100.")
    if max_states < 0:
        sys.exit("Max search states must be a positive integer.")
    if print_output != 0 and print_output != 1 and print_output != 2:
        sys.exit("Print output must be 0, 1 or 2.")

    THM(filename, target, max_states, print_output)
