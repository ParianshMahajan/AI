from collections import deque

j1 = int(input("Enter capacity of j1"))
j2 = int(input("Enter capacity of j2"))
target = int(input("Enter capacity of target"))

def waterJug():

    queue = deque([(0, 0)])
    visited = set([(0, 0)])

    while queue:
        amt1, amt2 = queue.popleft()
        print(amt1, amt2)

        if (amt1 == target and amt2 == 0) or (amt1 == 0 and amt2 == target):
            print("Target reached:", amt1, amt2)
            return True

        # Generate new states by pouring water from one jug to another
        new_states = [
            (j1, amt2),        # Fill jug 1
            (amt1, j2),        # Fill jug 2
            (0, amt2),         # Empty jug 1
            (amt1, 0),         # Empty jug 2
            (amt1 - min(amt1, j2 - amt2), amt2 + min(amt1, j2 - amt2)),  # Pour from jug 1 to jug 2
            (amt1 + min(amt2, j1 - amt1), amt2 - min(amt2, j1 - amt1))   # Pour from jug 2 to jug 1
        ]

        for state in new_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)

    print("Target not reachable.")
    return False

waterJug()