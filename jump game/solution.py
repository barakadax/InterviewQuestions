# https://leetcode.com/problems/jump-game/description/

from typing import Iterable

def can_jump(nums: Iterable[int]) -> bool:
    length = len(nums)
    target_index = length - 1

    for i in range(length-1, -1, -1):
        jump = nums[i]
        if i + jump >= target_index:
            target_index = i

    return target_index == 0
