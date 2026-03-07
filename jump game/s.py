# https://leetcode.com/problems/jump-game/description/

from typing import Iterable

# Time O(N) | Mem O(1) - Backwards
def can_jump(nums: Iterable[int]) -> bool:
    length: int = len(nums)
    target_index: int = length - 1

    for i in range(length-1, -1, -1):
        jump: int = nums[i]
        if i + jump >= target_index:
            target_index = i

    return target_index == 0


# Time O(N) | Mem O(1) - Forwards
def can_jump(nums: list[int]) -> bool:
    farthest: int = 0

    for i, jump in enumerate(nums):
        if i > farthest:
            return False

        farthest = max(farthest, i + jump)

    return True

print(can_jump([2,3,1,1,4])) # True
print(can_jump([3,2,1,0,4])) # False
