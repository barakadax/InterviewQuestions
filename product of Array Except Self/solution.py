# https://leetcode.com/problems/product-of-array-except-self/description/

from typing import Iterable

def product_except_self(nums: Iterable[int]) -> Iterable[int]:
    length = len(nums)
    left = [0]*length
    right = [0]*length
    l = 1
    r = 1

    for i in range(len(nums)):
        left[i] = l
        j = - i - 1
        right[j] = r
        l *= nums[i]
        r *= nums[j]

    return [l * r for l,r in zip(left, right)]
