problem = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

explored = [] # List to keep track of visited nodes.
frontier = []     #Initialize a queue

def bfs(explored, problem,startNode):
  explored.append(startNode)
  frontier.append(startNode)

  while frontier:
    node = frontier.pop(0) 
    print (node, end = " ") 

    for child in problem[node]:
      if child not in (explored and frontier):
        explored.append(child)
        frontier.append(child)

# Driver Code
bfs(explored, problem, 'A')