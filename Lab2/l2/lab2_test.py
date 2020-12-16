import unittest
import lab2
from lab2_utils import TextbookStack, apply_sequence

class TestLab2(unittest.TestCase):
    def testH(self):
        stack = TextbookStack(
            initial_order=[0, 1, 2, 3, 4, 6, 5, 7, 8],
            initial_orientations=[1, 1, 1, 0, 0, 1, 1, 1, 1]
        )

        node = lab2.Node(0, stack, None, 0)

        self.assertEqual(node.get_h(), 5)

    def testPQ(self):
        stack = TextbookStack(
            initial_order=[0, 2, 3, 5, 1, 4],
            initial_orientations=[0, 1, 0, 1, 0, 1]
        )

        visited_order = lab2.a_star_search(stack)

        isCorrect = True
        for i in range(len(visited_order)-1):
            print(visited_order[i].f, visited_order[i].name)
            if visited_order[i+1].f < visited_order[i].f:
                isCorrect = False
            elif visited_order[i+1].f == visited_order[i].f:
                if visited_order[i+1].name <= visited_order[i].name:
                    isCorrect = False
        self.assertTrue(isCorrect)