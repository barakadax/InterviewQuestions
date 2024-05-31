# https://leetcode.com/problems/last-stone-weight/description/

from typing import Iterable

def last_stone_weight(stones: Iterable[int]) -> int:
    stones = sorted(stones, reverse=True)

    while len(stones) > 1:
        stones = sorted(stones, reverse=True)
        first_max = stones[0]
        second_max = stones[1]
        temp = first_max - second_max

        for _ in range(2):
            del stones[0]

        if temp != 0:
            stones.append(temp)

    return stones[0] if stones else 0
