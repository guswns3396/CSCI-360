# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from collections import deque

def getState(stack):
    state = ''
    for i in stack.order:
        state += str(i)
    for i in stack.orientations:
        state+= str(i)
    return state

def enumerate(stack):
    states = []
    for i in range(stack.num_books):
        cpy = stack.copy()
        cpy.flip_stack(i + 1)
        states.append(cpy)
    return states

def breadth_first_search(stack):
    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #
    states_visited = {}
    if stack.check_ordered():
        return flip_sequence
    queue = deque([stack])
    states_visited[getState(stack)] = flip_sequence

    while len(queue) > 0:
        prev_stack = queue.popleft()
        prev_state = getState(prev_stack)
        possible_stacks = enumerate(prev_stack)
        for i in range(len(possible_stacks)):
            current_state = getState(possible_stacks[i])
            if current_state not in states_visited:
                states_visited[current_state] = [i for i in states_visited[prev_state]]
                states_visited[current_state].append(i+1)
                if possible_stacks[i].check_ordered():
                    return states_visited[current_state]
                queue.append(possible_stacks[i])
    # ---------------------------- #


def depth_first_search(stack):
    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #
    states_visited = {}
    if stack.check_ordered():
        return flip_sequence
    queue = deque([stack])
    states_visited[getState(stack)] = flip_sequence

    while len(queue) > 0:
        prev_stack = queue.pop()
        prev_state = getState(prev_stack)
        possible_stacks = enumerate(prev_stack)
        for i in range(len(possible_stacks)):
            current_state = getState(possible_stacks[i])
            if current_state not in states_visited:
                states_visited[current_state] = [i for i in states_visited[prev_state]]
                states_visited[current_state].append(i+1)
                if possible_stacks[i].check_ordered():
                    return states_visited[current_state]
                queue.append(possible_stacks[i])
    # ---------------------------- #
