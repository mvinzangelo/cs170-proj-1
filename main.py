import time
import copy
from heapq import heapify, heappush, heappop

class Board:
    def __init__(self, state, zero):
        self.state = state
        self.zero = zero
        self.n = 3

class Node:
    def __init__(self, val, depth = 0):
        self.val = val
        self.depth = depth
        self.a_star_val = 0
        self.children = []

    def __lt__(self, other):
        return self.a_star_val < other.a_star_val

class Eight_Puzzle_Problem: 
    initial_state = Board([[1,2,3],[4,5,6],[0,7,8]], {"x": 0, "y": 2})
    # initial_state = Board([[1,3,6],[5,0,2],[4,7,8]], {"x": 1, "y": 1})
    # initial_state = Board([[1,3,6],[5,0,7],[4,8,2]], {"x": 1, "y": 1})
    # initial_state = Board([[0,7,2],[4,6,1],[3,5,8]], {"x": 0, "y": 0})
    goal_state = Board([[1,2,3],[4,5,6],[7,8,0]], {"x": 2, "y": 2})

    # operators
    def move_up(self, board):
        if board.zero["y"] - 1 < 0:
            return False
        else:
            return True
    def move_down(self, board):
        if board.zero["y"] + 1 >= board.n:
            return False
        else:
            return True
    def move_left(self, board):
        if board.zero["x"] - 1 < 0: 
            return False
        else:
            return True
    def move_right(self, board):
        if board.zero["x"] + 1 >= board.n: 
            return False
        else:
            return True
    operators = [move_up, move_down, move_left, move_right]

    def goal_test(self, sample):
        return sample.state == self.goal_state.state

def move_zero(board, x_addition, y_addition):
    # create a deep copy of the input node
    new_board = copy.deepcopy(board)
    # store the previous x and y value
    old_x = new_board.zero["x"]
    old_y = new_board.zero["y"]
    # move the x and y value of the new board
    new_board.zero["x"] += x_addition
    new_board.zero["y"] += y_addition
    # swap move the zero towards the new direction
    new_board.state[old_y][old_x] = new_board.state[new_board.zero["y"]][new_board.zero["x"]]
    new_board.state[new_board.zero["y"]][new_board.zero["x"]] = 0
    return new_board


def expand(node, operators):
    # store which operators to expand on
    instructions = []
    # store the list of nodes to be enqueued
    node_list = []
    # create the list of viable operators
    for func in operators:
        instructions.append(func(operators, node.val))

    # add viable nodes to current node's children and node_list
    if instructions[0]:
        up_node = Node(move_zero(node.val, 0, -1), node.depth+1)
        node_list.append(up_node)
        node.children.append(up_node)
    if instructions[1]:
        down_node = Node(move_zero(node.val, 0, 1), node.depth+1)
        node_list.append(down_node)
        node.children.append(down_node)
    if instructions[2]:
        left_node = Node(move_zero(node.val, -1, 0), node.depth+1)
        node_list.append(left_node)
        node.children.append(left_node)
    if instructions[3]:
        right_node = Node(move_zero(node.val, 1, 0), node.depth+1)
        node_list.append(right_node)
        node.children.append(right_node)

    return node_list

def uniform_cost_heuristic(board):
    return 0

def misplaced_tile_heuristic(board):
    goal_state = [[1,2,3],[4,5,6],[7,8,0]]
    num_misplaced = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] != goal_state[i][j] and goal_state[i][j] != 0:
                num_misplaced += 1
    return num_misplaced

def manhattan_distance_heuristic(board):
    # hashmap for goal positions
    goal_positions = {
        1: {"x": 0, "y": 0},
        2: {"x": 1, "y": 0},
        3: {"x": 2, "y": 0},
        4: {"x": 0, "y": 1},
        5: {"x": 1, "y": 1},
        6: {"x": 2, "y": 1},
        7: {"x": 0, "y": 2},
        8: {"x": 1, "y": 2},
    }
    manhattan_distance = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            # find the difference between where the number should be currently and where it currently is
            if board[i][j] != 0 and goal_positions[board[i][j]] != {"x": j, "y": i}:
                manhattan_distance += abs(goal_positions[board[i][j]]["x"] - j)
                manhattan_distance += abs(goal_positions[board[i][j]]["y"] - i)
    return manhattan_distance

def a_star_enqueue(heuristic):
    def queueing_function(nodes, expanded_nodes):
        for x in expanded_nodes:
            # calculate a* value
            x.a_star_val = heuristic(x.val.state) + x.depth
            # push node into heap
            heappush(nodes, x)
        return nodes
    return queueing_function

def general_search(problem, queueing_function):
    # nodes = make_queue(make_node(problem.initial_state))
    nodes = [Node(problem.initial_state)]
    # loop do
    while nodes:
        # if nodes is empty then return failure
        if not nodes:
            return False
        # node = remove_front(nodes) 
        curr_node = nodes.pop(0)
        
        print("Depth: " + str(curr_node.depth) + " | A*: " + str(curr_node.a_star_val))
        for row in curr_node.val.state:
            print(row)

        # if problem.goal_test(node.state)
        if problem.goal_test(curr_node.val):
            return curr_node.val.state
        # nodes = queuing_function(nodes, EXPAND(node, problem.OPERATORS))
        nodes = queueing_function(nodes, expand(curr_node, problem.operators))
    # end

misplaced_tile_heuristic_enqueue = a_star_enqueue(misplaced_tile_heuristic)
manhattan_distance_heuristic_enqueue = a_star_enqueue(manhattan_distance_heuristic)
uniform_cost_enqueue = a_star_enqueue(uniform_cost_heuristic)
problem = Eight_Puzzle_Problem()
depth_0_board = Board([[1,2,3],[4,5,6],[7,8,0]], {"x": 2, "y": 2})
depth_4_board = Board([[1,2,3],[5,0,6],[4,7,8]], {"x": 1, "y": 1})
depth_8_board = Board([[1,3,6],[5,0,2],[4,7,8]], {"x": 1, "y": 1})
depth_12_board = Board([[1,3,6],[5,0,7],[4,8,2]], {"x": 1, "y": 1})
depth_16_board = Board([[1,6,7],[5,0,3],[4,8,2]], {"x": 1, "y": 1})
depth_20_board = Board([[7,1,2],[4,8,5],[6,3,0]], {"x": 2, "y": 2})
depth_24_board = Board([[0,7,2],[4,6,1],[3,5,8]], {"x": 0, "y": 0})
start_time = time.time()
general_search(problem, uniform_cost_search)
# general_search(problem, misplaced_tile_heuristic_enqueue)
# general_search(problem, manhattan_distance_heuristic_enqueue)
print("--- %s seconds ---" % (time.time() - start_time))