# Advent of Code
# Day: 6
# Author: Skusku
# Language: Python

# Sadly in a hurry, the solution for the first part got overwritten...

import unittest

input = "0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11"
example_input = "0	2	7	0"
hashes = dict()

def hash_list(lst_):
    return hash('-'.join(str(x) for x in lst_))

def format_input(ipt_):
    return [int(val) for val in ipt_.split('\t')]

def solve_part_1(ipt_):
    lst = format_input(ipt_)
    current_step = 0
    found = False
    while not found:
        print(lst)
        if step(lst, current_step):
            found = True
            break
        current_step += 1

    return current_step - hashes[hash_list(lst)]

def step(ipt_, step_cnt_):
    cnt = max(ipt_)
    max_index = ipt_.index(cnt)
    ipt_[max_index] = 0
    current_index = (max_index + 1) % len(ipt_)
    while cnt > 0:
        ipt_[current_index] += 1
        cnt -= 1
        current_index = (current_index + 1) % len(ipt_)

    hashed = hash_list(ipt_)
    try:
        if hashes[hashed]:
            return step_cnt_
    except KeyError:
        hashes[hashed] = step_cnt_
        return None



class TestSolution(unittest.TestCase):
    def test_solve_part_1(self):
        print(solve_part_1(input))
