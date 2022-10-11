# KEY POINTS: 
# - make sure to keep code general (can solve multiple n's for 8 puzzle)
# - make can put any inital state

class Node:
    def __init__(self, val):
        self.val = val
        self.children = [None]

class Eight_Puzzle_Problem: 
    initial_state = [[1,2,3],[4,5,6],[7,8,0]]
    goal_state = [[1,2,3],[4,5,6],[7,8,0]]
    def goal_test(self, sample):
        return sample == self.goal_state

def hit

def uniform_cost_search(nodes, expand_function)

    
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
            return curr_node.val
    #   nodes = queuing_function(nodes, EXPAND(node, problem.OPERATORS))
        nodes = 
    # end


problem = Eight_Puzzle_Problem()
print(general_search(problem, None))