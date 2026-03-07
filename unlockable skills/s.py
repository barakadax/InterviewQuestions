# Time O(N) | Space O(1)
def solution(T: list[int], A: list[int]) -> int:
    if not T:
        return 0

    if T[0] != -1:
        T[0] = -1

    for target in A:
        current: int = target

        while current != -1 and T[current] != -1:
            parent: int = T[current]
            T[current] = -1
            current = parent

        if current != -1 and T[current] == -1:
             if T[current] != -1:
                 T[current] = -1

    return T.count(-1)

# q: set[list[int]] = ([0, 0, 1, 1], [2]) # 3
q: set[list[int]] = ([0, 0, 0, 0, 2, 3, 3], [2, 5, 6]) # 5
# q: set[list[int]] = ([0, 0, 1, 2], [1, 2]) # 3
# q: set[list[int]] = ([0, 3, 0, 0, 5, 0, 5], [4, 2, 6, 1, 0]) # 7
# q: set[list[int]] = ([0, 3, 0, 0, 5, 0, 5], [4, 2, 6, 1, 0]) # 7

T: list[int] = q[0]
A: list[int] = q[1]

print(solution(T,A))
