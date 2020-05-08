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

    def initial_state(self):
        node = Node
        node.state = self.state
        node.action = self.returnActionArray(node)
        node.path_cost = 0
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
    child.parent = deepcopy(parent)
    child.action = action  # child chua action cua cha
    child.state = deepcopy(problem.result(parent, action))
    child.path_cost = parent.path_cost + problem.step_cost
    return child

def solution(solved):
    node = Node()
    node = deepcopy(solved)
    solutionAction = []

    while node.parent != None:
        solutionAction.insert(0,node.action)
        node = node.parent
    return solutionAction
    
def IDS(problem):
    for depth in range(15):
        result = DLS(problem, depth)
        if result != 'Fail':
            return result

def DLS(problem, limit):
    result = recursive_DLS(deepcopy(problem.initial_state()),problem,limit) #solution, failure/cutoff
    if result == 'cutoff' or result == 'failure':
        return 'Fail'
    else:
        return result

def recursive_DLS(node, problem, limit):
    if problem.goal_test(node) == 1:
        return solution(node)
    elif limit == 0:
        return 'cutoff'
    else:
        cutoff_occurred = False
        for action in problem.returnActionArray(node):
            childNode = deepcopy(child_node(problem, node, action))
            result = recursive_DLS(childNode, problem, limit-1)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result != 'failure':
                return result
        if cutoff_occurred:
            return 'cutoff'
        else:
            return 'failure'

problem = Problem()
node = Node()
node = problem.initial_state()
print(IDS(problem))
