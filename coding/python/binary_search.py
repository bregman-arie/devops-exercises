#!/usr/bin/env python

import random

rand_num_li = sorted([random.randint(1, 50) for iter in range(10)])
target = random.randint(1, 50)

def binary_search(li, le, ri, target):
    if le <= ri:
        mid = ri + le // 2
        if li[mid] == target:
            return mid
        elif li[mid] < target:
            return binary_search(li, mid + 1, ri, target)
        else:
            return binary_search(li, le, mid - 1, target)
    else:
        return -1


print("List: {}\nTarget: {}\nIndex: {}".format(
    rand_num_li, target,
    binary_search(rand_num_li, 0, len(rand_num_li) - 1, target)))
