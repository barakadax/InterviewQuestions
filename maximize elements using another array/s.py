import heapq

# Time O(N Log N) | Space O(N)
def solution(a: list[int], b: list[int]) -> list[int]:
    if not isinstance(a, list) or not isinstance(b, list) or not a or not b:
        raise ValueError("Expected 2 lists of numbers")

    unique_elements: set[int] = set(a) | set(b)

    return heapq.nlargest(len(a), unique_elements)

a = [2, 4, 3]
b = [5, 6, 1]

print(solution(a, b))
