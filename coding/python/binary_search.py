#!/usr/bin/env python

import random
from typing import List, Optional


def binary_search(arr: List[int], lb: int, ub: int, target: int) -> Optional[int]:
    """
    A Binary Search Example which has O(log n) time complexity.
    """
    while lb <= ub:
        mid = lb + (ub - lb) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lb = mid + 1
        else:
            ub = mid - 1
    return -1


def generate_random_list(size: int = 10, lower: int = 1, upper: int = 50) -> List[int]:
    return sorted(random.randint(lower, upper) for _ in range(size))


def find_target_in_list(target: int, lst: List[int]) -> int:
    return binary_search(lst, 0, len(lst) - 1, target)


def main():
    """
    Executes the binary search algorithm with a randomly generated list.
    Time Complexity: O(log n)
    """
    rand_num_li = generate_random_list()
    target = random.randint(1, 50)
    index = find_target_in_list(target, rand_num_li)
    print(f"List: {rand_num_li}\nTarget: {target}\nIndex: {index}")


if __name__ == '__main__':
    main()
