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
            # if the current tile is misplaced and is not 0, add 1 to the heuristic
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
    # ? benchmark code
    start_time = time.time()
    num_nodes = 0
    max_queue_size = 0
    expanded_nodes = []

    # nodes = make_queue(make_node(problem.initial_state))
    nodes = [Node(problem.initial_state)]
    # loop do
    while nodes:
        # if nodes is empty then return failure
        if not nodes:
            return False
        # node = remove_front(nodes) 
        curr_node = nodes.pop(0)
        
        # ? increase nodes expanded count
        num_nodes += 1
        
        # # ? print current node
        # print("Depth: " + str(curr_node.depth) + " | A*: " + str(curr_node.a_star_val))
        # for row in curr_node.val.state:
        #     print(row)

        # ? update max queue size
        if len(nodes) >= max_queue_size:
            max_queue_size = len(nodes)

        # if problem.goal_test(node.state)
        if problem.goal_test(curr_node.val):
            print("Number of nodes expanded: " + str(num_nodes))
            print("Max queue size: " + str(max_queue_size))
            print("Time: %s seconds" % (time.time() - start_time))
            return curr_node
        # nodes = queuing_function(nodes, EXPAND(node, problem.OPERATORS))
        if curr_node.val.state not in expanded_nodes: 
            nodes = queueing_function(nodes, expand(curr_node, problem.operators))
            expanded_nodes.append(copy.deepcopy(curr_node.val.state))
    # end

# test cases
depth_0_board = Board([[1,2,3],[4,5,6],[7,8,0]], {"x": 2, "y": 2})
depth_2_board = Board([[1,2,3],[4,5,6],[0,7,8]], {"x": 0, "y": 2})
depth_4_board = Board([[1,2,3],[5,0,6],[4,7,8]], {"x": 1, "y": 1})
depth_8_board = Board([[1,3,6],[5,0,2],[4,7,8]], {"x": 1, "y": 1})
depth_12_board = Board([[1,3,6],[5,0,7],[4,8,2]], {"x": 1, "y": 1})
depth_16_board = Board([[1,6,7],[5,0,3],[4,8,2]], {"x": 1, "y": 1})
depth_20_board = Board([[7,1,2],[4,8,5],[6,3,0]], {"x": 2, "y": 2})
depth_24_board = Board([[0,7,2],[4,6,1],[3,5,8]], {"x": 0, "y": 0})
test_cases = {
    0: depth_0_board,
    2: depth_2_board,
    4: depth_4_board,
    8: depth_8_board,
    12: depth_12_board,
    16: depth_16_board,
    20: depth_20_board,
    24: depth_24_board,
}

# enqueuing functions
misplaced_tile_heuristic_enqueue = a_star_enqueue(misplaced_tile_heuristic)
manhattan_distance_heuristic_enqueue = a_star_enqueue(manhattan_distance_heuristic)
uniform_cost_enqueue = a_star_enqueue(uniform_cost_heuristic)

problem = Eight_Puzzle_Problem()

# driver code
def main():
    board_is_unique = input("Would you like a unique board? (y/N): ")
    if board_is_unique.lower() == "n" or board_is_unique == "":
        board_number = input("Which board depth testcase would you like to test? (Enter 0, 2, 4, 8, 12, 16, 20 or 24): ")
        problem.initial_state = test_cases[int(board_number)]
    elif board_is_unique.lower() == "y":
        tmp_list = []
        print("Enter the board by row. Do not use any delimiting characters. Use a 0 to signify the empty block.")
        for i in range(0,3):
            tmp_list.append(input("Row " + str(i + 1) + ": "))
        board_state = [list(row) for row in tmp_list]
        board_zeros = None
        # find zero
        for i in range(3):
            for j in range(3):
                if board_state[i][j] == '0':
                    board_zeros = {"x": j, "y": i}
        # translate into ints
        board_state = [list(map(int, i)) for i in board_state]
        problem.initial_state = Board(board_state, board_zeros)
    heuristic = input("Which heuristic would you like to use?\n1 - Uniform Cost\n2 - Misplaced Tile\n3 - Manhattan Distance\nYour choice: ")
    if heuristic == '1':
        general_search(problem, uniform_cost_enqueue)
    elif heuristic == '2': 
        general_search(problem, misplaced_tile_heuristic_enqueue)
    elif heuristic == '3':
        general_search(problem, manhattan_distance_heuristic_enqueue)

if __name__ == "__main__":
    main()