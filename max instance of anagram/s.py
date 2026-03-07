from collections import defaultdict

# Time O(N) | Space O(N)
def solution(arr: list[str]) -> int:
    if not isinstance(arr, list) or len(arr) == 0:
        raise ValueError("Excepted a not empty list of strings")

    res_dict: defaultdict = defaultdict(int)
    max_counter: int = 0

    for i in arr:
        if not isinstance(i, str):
            raise ValueError("Excepted the list of strings to contain only strings")

        sorted_i: str = ''.join(sorted(i))
        res_dict[sorted_i] += 1

        if max_counter < res_dict[sorted_i]:
            max_counter = res_dict[sorted_i]

    return max_counter

print(solution(["abc","bca","cab","dab","bad"])) # 3
