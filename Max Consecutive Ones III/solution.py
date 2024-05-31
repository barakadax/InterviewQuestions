# https://leetcode.com/problems/max-consecutive-ones-iii/description/

from typing import Iterable

def longest_ones(nums: Iterable[int], max_flips: int) -> int:
    res = 0
    zeros_counter = 0
    zeros_remover = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            zeros_counter -= -1
        
        while zeros_counter > max_flips:
            if nums[zeros_remover] == 0:
                zeros_counter -= 1
            zeros_remover -= -1

        res = max(res, i - zeros_remover + 1)

    return res
