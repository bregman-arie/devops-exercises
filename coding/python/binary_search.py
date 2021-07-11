#!/usr/bin/env python

import random

def binary_search(arr, lb, ub, target):
    """
    A Binary Search Example which has O(log n) time complexity. 
    """
    if lb <= ub:
        mid = ub + lb // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, mid + 1, ub, target)
        else:
            return binary_search(arr, lb, mid - 1, target)
    else:
        return -1

if __name__ == '__main__':
    rand_num_li = sorted([random.randint(1, 50) for _ in range(10)])
    target = random.randint(1, 50)
    print("List: {}\nTarget: {}\nIndex: {}".format(
        rand_num_li, target,
        binary_search(rand_num_li, 0, len(rand_num_li) - 1, target)))
