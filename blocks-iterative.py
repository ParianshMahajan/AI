import copy

def is_goal_state(state):
    goal_state = [[['a', 'b', 'c'], [], []], [[], ['a', 'b', 'c'], []],[[], [], ['a', 'b', 'c']]]
    return state in goal_state


def action_taken(state, action):
    action_parts = action.split()
    block = action_parts[1]
    from_pos = action_parts[3]
    to_pos = action_parts[5]

    new_state = [list(row) for row in state]

    for row in new_state:
        if block in row:
            row.remove(block)
            break

    for row in new_state:
        if from_pos in row:
            row.remove(from_pos)
            break

    for row in new_state:
        if to_pos in row:
            row.append(block)
            break

    return new_state



def dls(state, actions, depth_limit):
    if depth_limit == 0:
        return 'Incomplete'
    if is_goal_state(state):
        return 'Goal Achieved'

    for action in actions:
        new_state = action_taken(state, action)
        result = dls(new_state, actions, depth_limit - 1)
        if result == 'Goal Achieved':
            return result

    return 'Incomplete'

def iteration_dls(state,actions):
    depth=0
    while True:
        result =dls(state,actions,depth)
        if(result=='Goal Achieved'):
            return depth
        depth+=1
    



initial_state = [[['b'], ['c', 'a'], []]]
actions = ["Move A from X to Y", "Move B from X to Y", "Move C from X to Y"]
x = iteration_dls(initial_state, actions)
print(x)
