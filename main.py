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
        
    
    

    
def general_search(problem, queueing_function):
    # nodes = make_queue(make_node(problem.initial_state))
    # loop do
    #       if nodes is empty then return failure
    #   node = remove_front(nodes) 
    #       if problem.goal_test(node.state)
    #   nodes = queuing_function(nodes, EXPAND((problem.OPERATORS))
    # end
    print(problem.goal_test([[1,2,2],[4,5,6],[7,8,0]]))
    


problem = Eight_Puzzle_Problem()
general_search(problem, None)