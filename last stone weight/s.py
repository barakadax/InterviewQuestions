# https://leetcode.com/problems/last-stone-weight/description/

import heapq

# Time O(N log N) | Mem O(N)
def last_stone_weight(stones: list[int]) -> int:
    max_heap: list[int] = [-s for s in stones]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        first: int = heapq.heappop(max_heap)
        second: int = heapq.heappop(max_heap)

        if first != second:
            heapq.heappush(max_heap, first - second)

    return -max_heap[0] if max_heap else 0

print(last_stone_weight([2,7,4,1,8,1])) # 1
print(last_stone_weight([1])) # 1
