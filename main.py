# KEY POINTS: 
# - make sure to keep code general (can solve multiple n's for 8 puzzle)
# - make can put any inital state

class Board:
    def __init__(self, state, zero):
        self.state = state
        self.zero = zero
        self.n = 3

class Node:
    def __init__(self, val):
        self.val = val
        self.children = [None]

class Eight_Puzzle_Problem: 
    initial_state = Board([[1,2,3],[4,5,6],[7,8,0]], {"x": 2, "y": 2})
    goal_state = Board([[1,2,3],[4,5,6],[7,8,0]], {"x": 2, "y": 2})

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

def expand(node, operators):
    instructions = []
    node_list = []
    for func in operators:
        instructions.append(func(operators, node.val))

    # if instructions[0]:
        
        

# def uniform_cost_search(nodes, expand_function)

    
def general_search(problem, queueing_function):
    # nodes = make_queue(make_node(problem.initial_state))
    nodes = [Node(problem.initial_state)]
    # loop do
    while nodes:
    #       if nodes is empty then return failure
        if not nodes:
            return False
    #   node = remove_front(nodes) 
        curr_node = nodes.pop(0)
    #   if problem.goal_test(node.state)
        if problem.goal_test(curr_node.val):
            return curr_node.val.state
    #   nodes = queuing_function(nodes, EXPAND(node, problem.OPERATORS))
        nodes = queueing_function(nodes, expand(node, problem.operators))
    # end


problem = Eight_Puzzle_Problem()
test_board = Board([[1,2,3],[4,5,6],[7,8,0]], {"x": 2, "y": 2})
test_node = Node(test_board)
expand(test_node, problem.operators)
