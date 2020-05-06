import numpy as np
import itertools
list2d = [[1,2,3], [4,5,6], [7], [8,9]]
merged = list(itertools.chain.from_iterable(list2d))

class Node:
  state = None
  parent = None
  path_cost = None
  action = None

class Problem:
  col = {0:'RIGHT', 2: 'LEFT', 1: ['LEFT', 'RIGHT']}
  row = {0:'DOWN', 2: 'UP', 1: ['UP', 'DOWN']}
  step_cost = 1

#   stateString = [['3','1','2'],
#            ['6','','8'],
#            ['7','5','4']]
#   goalString = [['','1','2'],
#                 ['3','4','5'],
#                 ['6','7','8']]
  state = np.array([[3,1,2],
                    [6,'',8],
                    [7,5,4]])
  goal = np.array([['',1,2],
                    [3,4,5],
                    [6,7,8]])
  def returnBlankIndex(self, node):
    return np.where(node.state == '')

  def returnActionArray(self, node):
    index = self.returnBlankIndex(node)
    rowindex = index[0].item()
    colindex = index[1].item()
    action = []
    action.append(self.row[rowindex])
    action.append(self.col[colindex])
    action = list(itertools.chain.from_iterable(action))
    return action

  def initial_state(self):
    node = Node
    node.state = self.state
    node.action = self.returnActionArray(node)
    node.path_cost = 0
    return node
  def goal_test(self, node):
    if(self.goal.all() and node.state.all()):
      return 1
    else:
      return 0
  #Viet ham Result child state
  def result(self, node, action):
    index = self.returnBlankIndex(node)
    rowBlankindex = index[0].item()
    colBlankindex = index[1].item()
    
    if action == 'UP':
      rowindex = rowBlankindex - 1
      colindex = colBlankindex
    elif action == 'DOWN':
      rowindex = rowBlankindex + 1
      colindex = colBlankindex
    elif action == 'LEFT':
      rowindex = rowBlankindex
      colindex = colBlankindex - 1
    elif action == 'RIGHT':
      rowindex = rowBlankindex
      colindex = colBlankindex + 1
    node.state[rowindex][colindex], node.state[rowBlankindex][colBlankindex] = node.state[rowindex][colindex], node.state[rowBlankindex][colBlankindex]
    return node.state
  
  
def child_node(problem, parent, action):
  child = Node()
  child.parent = parent
  child.action = action #child chua action cua cha
  child.state = problem.result(parent, action)
  child.path_cost = parent.path_cost + problem.step_cost
  return child

def UCS(problem):
  node = Node()
  node = problem.initial_state()
  print(node.state)
  frontier = [node]
  explored = []
  while(1):
    if(frontier != []):
      return 0
    else:
      min_path_cost = 1000000
      indexPop = None
      for checkNode in frontier:
        if(min_path_cost < checkNode.path_cost):
          indexPop = frontier.index(checkNode)
          min_path_cost = checkNode.path_cost
      node = frontier.pop(indexPop)
      
    if(problem.goal_test(node)):
      return "Ra dap an"
    else:
      explored.append(node.state)
    
    for action in problem.returnActionArray(node):
      childNode = child_node(problem, node, action)
      #check state
      if childNode not in (explored and frontier):
        frontier.append(childNode)

    
problem = Problem()
node = Node()
node = problem.initial_state()
print(problem.goal_test(node))
#UCS(problem)