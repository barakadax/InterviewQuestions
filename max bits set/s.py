from collections import defaultdict

# Time O(N) | Space O(1)
def solution(arr: list[int] | None) -> int:
    if not isinstance(arr, list) or len(arr) < 2:
        raise ValueError("Expected array of at least 2 elements")

    bit_counts: defaultdict = defaultdict(int)
    for num in arr:
        if not isinstance(num, int):
            raise ValueError("All elements must be integers")

        n: int = abs(num)

        position: int = 0
        while n > 0:
            if n & 1:
                bit_counts[position] += 1
            n >>= 1
            position += 1

    return max(bit_counts.values()) if bit_counts else 0

print(solution([13,8,2,7,3]))
