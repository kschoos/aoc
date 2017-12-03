# Advent of Code
# Day: 3
# Author: Skusku
# Language: Python

import unittest
import math

def solve(input):
    # Use Gaussian sum to calculate the layer of the current input ( n(n+1)/2 = k )
    # As every layer has layer*8 values in it, we set k = 2*(8*layer) = n(n+1) and solve the
    # quadratic equation
    layer = math.ceil( (-1 + math.sqrt(1 + 4 * (math.ceil((input-1)/4))))/2 )
    # Last value of the previous layer and layer depth
    last_layer_end = (layer*(layer-1))*4 + 1
    layer_depth = layer * 8
    # Find the first center (The value in this layer, directly right of the '1')
    first_center = last_layer_end + layer
    # Finally find the closest center. Every center is layer_depth/4 steps away from each other.
    min_distance = min([abs(input - (first_center + idx * (layer_depth/4))) for idx in range(4)])
    return min_distance + layer

class TestSolution(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solve(1), 0)
        self.assertEqual(solve(12), 3)
        self.assertEqual(solve(23), 2)
        self.assertEqual(solve(1024), 31)

        print("The winner is: {}".format(solve(265149)))

if __name__ == '__main__':
    unittest.main()
