def heuristic(graph,current_node,visited,start_node):
    unvisited = set(graph.keys()) - visited
    if len(unvisited)==0:
        return graph[current_node][start_node]
    return min(graph[current_node].get(n,float('inf')) for n in unvisited)
