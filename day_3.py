# Advent of Code
# Day: 3
# Author: Skusku
# Language: Python

import unittest
import math

def solve_part_1(input):
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

# Find the first value that is larger than the given value
# Run through the spiral and sum.
def solve_part_2(value):
    values = dict()

    col = 0
    row = 0
    dir = 1
    walked = 0
    depth = 2
    sign = 1


    values[(col, row)] = 1
    last_value = 1

    while last_value < value:
        sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                try:
                    sum += values[(col+i, row+j)]
                except:
                    pass
        if not ( col == 0 and row == 0):
            values[(col, row)] = sum
        last_value = sum

        if dir == 1:
            col += sign

        elif dir == -1:
            row += sign

        walked += 1
        if walked == depth/2:
            dir = -dir
        if walked == depth:
            dir = -dir
            sign = -sign
            depth += 2
            walked = 0

    return last_value


class TestSolution(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(solve_part_1(1), 0)
        self.assertEqual(solve_part_1(12), 3)
        self.assertEqual(solve_part_1(23), 2)
        self.assertEqual(solve_part_1(1024), 31)

        print("The winner for part 1 is: {}".format(solve_part_1(265149)))

    def test_part_2(self):
        self.assertEqual(solve_part_2(118), 122)
        self.assertEqual(solve_part_2(300), 304)
        self.assertEqual(solve_part_2(748), 806)
        print("The winner for part 2 is: {}".format(solve_part_2(265149)))

if __name__ == '__main__':
    unittest.main()
