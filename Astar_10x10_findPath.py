
import itertools
from copy import deepcopy
import time
import math
start_time = time.time()

class Node():
    state = None  #position
    parent = None
    path_cost = 0
    action = None
    heuristic = 0
    cost_estimate = 0

class Problem():
    action = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    step_cost = 1
    maze =     [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],  # 1: obstacle position
                [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

    state = (0, 0)
    goal = (8, 9)

    def returnActionArray(self, node):
        nodeindex = node.state  #state is position
        action = []
        for newAction in self.action:
            newState = (nodeindex[0] + newAction[0], nodeindex[1] + newAction[1])
            if (newState[0] > (len(self.maze) - 1) or newState[0] < 0 or newState[1] > (len(self.maze[len(self.maze)-1]) -1) or newState[1] < 0):
                continue
            if (self.maze[newState[0]][newState[1]] != 0):
                continue
            if(newAction == self.action[0]):
                action.append("LEFT")
            elif(newAction == self.action[1]):
                action.append("RIGHT")
            elif(newAction == self.action[2]):
                action.append("UP")
            elif(newAction == self.action[3]):
                action.append("DOWN")
        return action

    def distance_heuristic(self, node):
        cost_estimate = math.sqrt((node.state[0] - self.goal[0])**2 + (node.state[1] - self.goal[1])**2)
        return cost_estimate

    def initial_state(self):
        node = Node()
        node.state = self.state
        node.action = self.returnActionArray(node)
        node.path_cost = 0
        node.heuristic = self.distance_heuristic(node)
        node.cost_estimate = node.path_cost + node.heuristic
        return node

    def goal_test(self, node):
        if node.state != self.goal:
            return 0
        else:
            return 1

    def result(self, parentState, action):
        newState = deepcopy(parentState)
        if action == 'UP':
            newState = (newState[0] - 1, newState[1])
        elif action == 'DOWN':
            newState = (newState[0] + 1, newState[1])
        elif action == 'LEFT':
            newState = (newState[0], newState[1] - 1)
        elif action == 'RIGHT':
            newState = (newState[0], newState[1] + 1)
        return newState
    
def child_node(problem, parent, action):
    child = Node()
    child.parent = parent
    child.action = action  # child chua action cua cha
    child.state = problem.result(parent.state, action)
    child.path_cost = parent.path_cost + problem.step_cost
    child.heuristic = problem.distance_heuristic(child)
    child.cost_estimate = child.path_cost + child.heuristic
    return child

def checkInExplored(explored, nodeState):
    lenExplored = len(explored)
    for i in range(lenExplored):
        if nodeState == explored[i]:
            return 1
    return 0

def checkInFrontier(frontier, node):
    lenFrontier = len(frontier)
    for i in range(lenFrontier):
        if node.state == frontier[i].state:
            return 1
    return 0

def changeIfCostEstimateLess(frontier, childNode):
    lenFrontier = len(frontier)
    for i in range(lenFrontier):
        if childNode.state == frontier[i].state:
            if childNode.cost_estimate < frontier[i].cost_estimate:
                frontier[i] = (child_node)
            break

def solution(solved):
    node = Node()
    node = solved
    solutionAction = []
    while node.parent is not None:
        solutionAction.insert(0,node.state)
        node = node.parent
    return solutionAction

def Astar(problem):
    node = Node()
    node = problem.initial_state()
    frontier = [node]
    explored = []
    while(1):
        if len(frontier) <= 0:
            return 0
        else:
            print('frontier len: ',len(frontier))
            min_cost_estimate = 1000000
            indexPop = int()
            for checkNode in frontier:
                if(checkNode.cost_estimate < min_cost_estimate):
                    indexPop = frontier.index(checkNode)
                    min_cost_estimate = checkNode.cost_estimate
            node = (frontier.pop(indexPop))
            print("---------------------")
            print('node ',node.state)
        if problem.goal_test(node) == 1:
            return solution(node)
        else:
            explored.append(node.state)
        for action in problem.returnActionArray(node):
            childNode = (child_node(problem, node, action))
            childInFrontier = checkInFrontier(frontier, childNode)
            childInExplored = checkInExplored(explored, childNode.state)

            print("---------------------")
            print(action)
            print('child',childNode.state)
            print('childCost_estimate', childNode.cost_estimate)
            if childInFrontier == 0 and childInExplored == 0:  # error
                frontier.append(childNode)
            elif childInFrontier == 1:
                changeIfCostEstimateLess(frontier, childNode)

if __name__ == '__main__':
    problem = Problem()  
    print(Astar(problem))
    print("--- %s seconds ---" % (time.time() - start_time))