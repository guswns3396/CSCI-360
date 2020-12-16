# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from heapq import heappush, heappop

def get_state(stack):
    state = ''
    for i in stack.order:
        state += str(i)
    for i in stack.orientations:
        state += str(i)
    return state

class Node:
    count = 0

    def __init__(self, g, stack, parent, flip):
        self.g = g
        self.name = Node.count
        self.stack = stack
        self.state = get_state(stack)
        self.parent = parent
        self.flip = flip
        self.f = self.g + self.get_h()
        Node.count += 1

    def get_h(self):
        def is1(order):
            diff = order[0] - order[1]
            return not (diff == 1 or diff == -1)
        def is2(orient):
            return orient[0] != orient[1]
        def is3(pair, orient):
            return (pair[0] + 1 != pair[1]) and (orient[0] and orient[1])
        def is4(pair, orient):
            return (pair[0] + 1 == pair[1]) and (not orient[0] and not orient[1])

        h = 0
        for i in range(self.stack.num_books-1):
            order = self.stack.order[i:i+2]
            orient = self.stack.orientations[i:i+2]
            if is1(order) or is2(orient) or is3(order, orient) or is4(order, orient):
                h += 1
        return h

def a_star_search(stack):

    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #
    # push initial state to pq
    # while pq not empty
        # pop state from pq
        # check if goal state
            # trace for flip sequence & return
        # expand nodes from state
        # check if expanded nodes visited
        # enqueue nodes from state

    pq = []
    visited = set({})

    ### testing ###
    # visit_order = []
    ### testing ###

    node = Node(0, stack, None, 0)
    visited.add(node.state)
    entry = [node.f, node.name, node]
    heappush(pq, entry)

    while len(pq) > 0:
        # get next node from fringe
        entry = heappop(pq)
        node = entry[-1]

        ### testing ###
        # visit_order.append(node)
        ### testing ###

        # check if goal node & trace
        if node.stack.check_ordered():
            while node.parent is not None:
                flip_sequence.append(node.flip)
                node = node.parent
            Node.count = 0

            ### testing ###
            # flip_sequence = visit_order[::-1]
            ### testing ###

            return flip_sequence[::-1]

        # enumerate child nodes
        for i in range(stack.num_books):
            cpy = node.stack.copy()
            cpy.flip_stack(i+1)
            # add to fringe
            state = get_state(cpy)
            new_node = Node(node.g+1, cpy, node, i+1)
            if state not in visited:
                visited.add(new_node.state)
                entry = [new_node.f, new_node.name, new_node]
                heappush(pq, entry)

    return flip_sequence
    # ---------------------------- #


def weighted_a_star_search(stack, epsilon=None, N=1):
    # Weighted A* is extra credit

    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #

    return flip_sequence

    # ---------------------------- #
