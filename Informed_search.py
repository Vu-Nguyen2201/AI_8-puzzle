#Họ và Tên: Nguyễn Tuấn Vũ
#MSSV: 18133064
#Lớp: Trí tuệ nhân tạo sáng thứ 3
#Giảng viên hướng dẫn: Trần Nhật Quang
#Nội dung bài tập: Tuần 06
#Đã sao lưu trên git: https://github.com/Vu-Nguyen2201/AI_8-puzzle
#Tham khảo: 
#[1] Stuart J. Russell and Peter Norvig. (2016). Artificial Intelligence A Modern Approach Third Edition
#[2] Thầy Trần Nhật Quang (2020). Môn Trí tuệ nhân tạo - Video bài giảng tuần 06

import numpy as np
import itertools
from copy import deepcopy

class Node:
    state = None
    parent = None
    path_cost = None
    action = None
    heuristic = None

class Problem:
    col = {0: ['RIGHT'], 2: ['LEFT'], 1: ['LEFT', 'RIGHT']}
    row = {0: ['DOWN'], 2: ['UP'], 1: ['UP', 'DOWN']}
    step_cost = 1

    state = np.array([[3, 1, 2],
                      [6, '', 8],
                      [7, 5, 4]])
    goal = np.array([['', 1, 2],
                     [3, 4, 5],
                     [6, 7, 8]])

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

    def heuristic_9(self, node):
        return (node.state == self.goal).sum()

    def initial_state(self):
        node = Node
        node.state = self.state
        node.action = self.returnActionArray(node)
        node.path_cost = 0
        node.heuristic = self.heuristic_9(node)
        return node

    def goal_test(self, node):
        check = node.state == self.goal
        if False in check:
            return 0
        else:
            return 1

    def result(self, node, action):
        index = self.returnBlankIndex(node)
        rowBlankindex = index[0].item()
        colBlankindex = index[1].item()
        Anode = Node()
        Anode.state = deepcopy(node.state)
        rowindex = 0
        colindex = 0
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
        Anode.state[rowindex][colindex], Anode.state[rowBlankindex][colBlankindex] = Anode.state[rowBlankindex][colBlankindex], Anode.state[rowindex][colindex]
        return Anode.state

def child_node(problem, parent, action):
    child = Node()
    child.parent = (parent)
    child.action = action  # child chua action cua cha
    child.state = (problem.result(parent, action))
    child.path_cost = parent.path_cost + problem.step_cost
    return child

def checkInExplored(explored, nodeState):
    lenExplored = len(explored)
    for i in range(lenExplored):
        check = nodeState == explored[i]
        if check.all() == True:
            return 1
    return 0

def checkInFrontier(frontier, node):
    lenFrontier = len(frontier)
    for i in range(lenFrontier):
        check = node.state == frontier[i].state
        if check.all() == True:
            return 1
    return 0

def changeIfPathCostLess(frontier, childNode):
    lenFrontier = len(frontier)
    for i in range(lenFrontier):
        check = childNode.state == frontier[i].state
        if check.all() == True:
            if childNode.path_cost < frontier[i].path_cost:
                frontier[i] = (child_node)
            break
def changeIfHeuristicLess(frontier, childNode):
    lenFrontier = len(frontier)
    for i in range(lenFrontier):
        check = childNode.state == frontier[i].state
        if check.all() == True:
            if childNode.heuristic < frontier[i].heuristic:
                frontier[i] = (child_node)
            break

def solution(solved):
    node = Node()
    node = (solved)
    solutionAction = []

    while node.parent != None:
        solutionAction.insert(0,node.action)
        node = node.parent
    return solutionAction

def UCS(problem):
    node = Node()
    node = (problem.initial_state())
    frontier = [node]
    explored = []
    while(1):
        if len(frontier) <= 0:
            return 0
        else:
            print(len(frontier))

            # min_path_cost = 1000000
            # indexPop = int()
            # for checkNode in frontier:
            #     if(checkNode.path_cost < min_path_cost):
            #         indexPop = frontier.index(checkNode)
            #         min_path_cost = checkNode.path_cost
            # node = (frontier.pop(indexPop))

            min_heuristic = 1000000
            indexPop = int()
            for checkNode in frontier:
                if(checkNode.heuristic < min_heuristic):
                    indexPop = frontier.index(checkNode)
                    min_heuristic = checkNode.heuristic
            node = (frontier.pop(indexPop))
            
            print("---------------------")
            print('node ',node.state)
        if(problem.goal_test(node) == 1):
            return solution(node)
        else:
            explored.append((node.state)) #Stack: LIFO - BFS

        for action in problem.returnActionArray(node):
            childNode = (child_node(problem, node, action))
            childInFrontier = checkInFrontier(frontier, childNode)
            childInExplored = checkInExplored(explored, childNode.state)
            print("---------------------")
            print(action)
            print('child',childNode.state)
            print('childPathCost', childNode.path_cost)
            if childInFrontier == 0 and childInExplored == 0:  # error
                frontier.append((childNode))
            elif childInFrontier == 1:
                changeIfHeuristicLess(frontier, childNode)

problem = Problem()
node = Node()
node = problem.initial_state()
print(UCS(problem))