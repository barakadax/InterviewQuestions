# https://leetcode.com/problems/max-consecutive-ones-iii/description/

from typing import Iterable

# Time O(N) | Mem O(1)
def longest_ones(nums: list[int], max_flips: int) -> int:
    left: int = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            max_flips -= 1

        if max_flips < 0:
            if nums[left] == 0:
                max_flips += 1
            left += 1

    return len(nums) - left

print(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
print(longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)) # 10
