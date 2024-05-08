def solve(graph, startLoc):
    visited = []
    dist = 0
    visited.append(startLoc)
    
    while len(visited) != len(graph):
        nextNode, cost = findNearest(graph, visited, visited[-1])
        visited.append(nextNode)
        dist += cost
    
    currLoc = visited[-1]
    lastList = graph[currLoc - 1]
    
    for element in lastList:
        node, nextNode, cost = element
        if nextNode == visited[0]:
            visited.append(nextNode)
            dist += cost
            
    return visited, dist
        
        
def findNearest(graph, visited, currLoc):
    
    sublist = graph[currLoc-1]
    sortedSubList = sorted(sublist, key=lambda x: x[2])
    
    for element in sortedSubList:
        
        node, nextNode, cost = element
        if(nextNode not in visited):
            return nextNode, cost
    
graph = [
        [[1, 2, 10], [1, 3, 15], [1, 4, 20]],
        [[2, 1, 10], [2, 3, 35], [2, 4, 25]],
        [[3, 4, 30], [3, 1, 15], [3, 2, 35]],
        [[4, 1, 20], [4, 2, 25], [4, 3, 30]]
        ]

startLoc = 4
print(solve(graph, startLoc))