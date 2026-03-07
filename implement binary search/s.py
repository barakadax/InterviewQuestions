# Time O(Log N) | Space O(Log N) - Recursive
def find_num(arr: list[int], target_num: int, min_index: int, max_index: int) -> int:
    if (
        not isinstance(arr, list)
        or len(arr) < 2
        or not all(isinstance(i, int) for i in [target_num, min_index, max_index])
    ):
        return -1

    index: int = int((min_index + max_index) / 2)
    temp: int = arr[index]

    if temp == target_num:
        return index
    elif min_index == index or max_index == index:
        return -1
    elif temp > target_num:
        max_index = index
        return find_num(arr, target_num, min_index, max_index)

    min_index = index
    return find_num(arr, target_num, min_index, max_index)


# Time (Log N) | Space O(1)- Loop
def find_num(arr: list[int], target_num: int, min_index: int, max_index: int) -> int:
    if (
        not isinstance(arr, list)
        or len(arr) < 2
        or not all(isinstance(i, int) for i in [target_num, min_index, max_index])
    ):
        return -1

    while min_index <= max_index:
        index: int = (min_index + max_index) // 2

        if index < 0 or index >= len(arr):
            break

        temp: int = arr[index]

        if temp == target_num:
            return index
        elif temp > target_num:
            max_index = index - 1
        else:
            min_index = index + 1

    return -1


arr: list[int] = [0, 1, 5, 7, 9]
target_num: int = 10
min_index: int = 0
max_index: int = len(arr) - 1

print(f"res: {find_num(arr, target_num, min_index, max_index)}")
