import numpy as np
# class a:
#     a = np.array([[3,1,2], [6,0,8], [7,5,4]])
#     x = 4

# class b:
#     b = np.array([[3,1,2], [6,0,8], [7,5,4]])
#     x = 5
# class c:
#     b = np.array([[3,1,2], [6,0,8], [7,5,4]])
#     x = 9
# #check object element in list elements of boject
# goal = b()
# state = a()
# x = c()
# li = [state, x, x]
# li.append(x)
# check = goal.b in li[1].b
# print(len(li))

# List1
# List1 = [[1,2],[3,4]]
 
# # List2
# List2 = [[1,2]]
# length = len(List1)

# s = set()
# s.add(List1[0])
# s.add(List1[1])
# if List2 in s:
#     print('yes')
#check =  all(item in List1 for item in List2
import numpy as np
import math
# a = np.array([1, 1, 3, 3])
# b = np.array([1, 2, 4, 3])

# print((a == b).sum())
state = np.array([[3, 1, 2],
                      [6, '', 8],
                      [7, 5, 4]])
goal = np.array([['', 1, 2],
                    [3, 4, 5],
                    [6, 7, 8]])
cost_estimate = 0
for i in range(3):
    for j in range(3):
        indexGoal = np.where(goal == state[i][j])
        rowindex = indexGoal[0].item()
        colindex = indexGoal[1].item()
        cost_estimate = cost_estimate + math.fabs(i - rowindex) + math.fabs(j - colindex)
        print(cost_estimate)