import itertools

class TSP:
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.visited = set()
        self.path = []
        self.total_cost = 0

    def heuristic(self, node):
        # Calculate the minimum spanning tree (MST) heuristic
        unvisited = set(self.graph.keys()) - self.visited
        if len(unvisited) == 0:
            return self.graph[node][self.start]
        return min(self.graph[node][n] for n in unvisited)

    def a_star(self):
        open_list = [(0, self.start)]
        while open_list:
            cost, current_node = min(open_list)
            open_list.remove((cost, current_node))
            if current_node in self.visited:
                continue
            self.path.append(current_node)
            self.visited.add(current_node)
            if len(self.visited) == len(self.graph):
                self.total_cost += self.graph[current_node][self.start]
                self.path.append(self.start)
                return self.path, self.total_cost
            for neighbor, distance in self.graph[current_node].items():
                if neighbor not in self.visited:
                    heuristic = self.heuristic(neighbor)
                    open_list.append((distance + heuristic, neighbor))
            self.total_cost += cost
        return None, None

# Example usage
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}
start_node = 'A'
tsp = TSP(graph, start_node)
path, cost = tsp.a_star()
print("Path:", path)
print("Total Cost:", cost)
