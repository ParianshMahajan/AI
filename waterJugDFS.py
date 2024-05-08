from collections import defaultdict

j1 = int(input("Enter capacity of j1"))
j2 = int(input("Enter capacity of j2"))
target = int(input("Enter capacity of target"))

visited = defaultdict(lambda: False)

def waterJug(amt1, amt2):
    if (amt1 == target and amt2 == 0) or (amt1 == 0 and amt2 == target):
        print(amt1, amt2)
        return True

    if visited[(amt1, amt2)] == False:
        print(amt1, amt2)
        visited[(amt1, amt2)] = True
        # Generate new states by pouring water from one jug to another
        states = [
            (j1, amt2),  # Fill jug 1
            (amt1, j2),  # Fill jug 2
            (0, amt2),   # Empty jug 1
            (amt1, 0),   # Empty jug 2
            (amt1 - min(amt1, j2 - amt2), amt2 + min(amt1, j2 - amt2)),  # Pour from jug 1 to jug 2
            (amt1 + min(amt2, j1 - amt1), amt2 - min(amt2, j1 - amt1))   # Pour from jug 2 to jug 1
        ]
        for state in states:
            if waterJug(state[0], state[1]):
                return True

    return False

waterJug(0, 0)