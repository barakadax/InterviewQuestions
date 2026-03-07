# https://leetcode.com/problems/product-of-array-except-self/description/

# Time O(N) | Mem O(1)
def product_except_self(nums: list[int]) -> list[int]:
    res: list[int] = [1] * len(nums)

    prefix: int = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    suffix: int = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res

print(product_except_self([1,2,3,4])) # [24,12,8,6]
print(product_except_self([-1,1,0,-3,3])) # [0,0,9,0,0]
