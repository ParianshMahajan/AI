import itertools

def heuristic(graph, visited, current_node, start):
    unvisited = set(graph.keys()) - visited
    if len(unvisited) == 0:
        return graph[current_node][start]
    return min(graph[current_node].get(n, float('inf')) for n in unvisited)

def a_star(graph, start):
    visited = set()
    path = []
    total_cost = 0
    open_list = [(0, start)]

    while open_list:
        cost, current_node = min(open_list)
        open_list.remove((cost, current_node))
        if current_node in visited:
            continue
        path.append(current_node)
        visited.add(current_node)
        if len(visited) == len(graph):
            total_cost += graph[current_node][start]
            path.append(start)
            return path, total_cost
        for neighbor, distance in graph[current_node].items():
            if neighbor not in visited:
                h = heuristic(graph, visited, neighbor, start)
                open_list.append((distance + h, neighbor))
        total_cost += cost

    return None, None

# Example usage
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}
start_node = 'A'
path, cost = a_star(graph, start_node)
print("Path:", path)
print("Total Cost:", cost)
