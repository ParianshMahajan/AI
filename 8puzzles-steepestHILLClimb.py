import sys
import copy

def compare(s, g):
    if s == g:
        return True
    else:
        return False

def find_pos(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return [i, j]

def up(s, pos):
    i = pos[0]
    j = pos[1]
    if i > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i - 1][j]
        temp[i - 1][j] = 0
        return temp
    else:
        return s

def down(s, pos):
    i = pos[0]
    j = pos[1]
    if i < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i + 1][j]
        temp[i + 1][j] = 0
        return temp
    else:
        return s

def left(s, pos):
    i = pos[0]
    j = pos[1]
    if j > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j - 1]
        temp[i][j - 1] = 0
        return temp
    else:
        return s

def right(s, pos):
    i = pos[0]
    j = pos[1]
    if j < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j + 1]
        temp[i][j + 1] = 0
        return temp
    else:
        return s

def enqueue(s, val):
    global q
    q = q + [(val, s)]

def heuristic(s, g):
    d = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != g[i][j]:
                d += 1
    return d

def search(s, g):
    curr_state = copy.deepcopy(s)
    if s == g:
        return
    global visited
    while True:
        pos = find_pos(curr_state)
        neighbors = [up(curr_state, pos), down(curr_state, pos), left(curr_state, pos), right(curr_state, pos)]
        min_neighbor = min(neighbors, key=lambda x: heuristic(x, g))
        if min_neighbor != curr_state:
            if min_neighbor == g:
                print("found the intermediate states are: ")
                print(visited + [g])
                return
            else:
                enqueue(min_neighbor, heuristic(min_neighbor, g))
                curr_state = min_neighbor
        else:
            print("not found")
            return

def main():
    s = [[2, 0, 2], [1, 8, 4], [7, 6, 5]]
    g = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    global q
    global visited
    q = []
    visited = [s]
    search(s, g)

if __name__ == "__main__":
    main()
