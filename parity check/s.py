from textwrap import dedent

# Time O(N power 2) | Mem O(1)
def check_parity(matrix: list[list[str]]) -> str:
    n: int = len(matrix)
    odd_row: int = -1
    odd_col: int = -1

    for i in range(n):
        row_sum: int = sum(matrix[i])
        if row_sum % 2 != 0:
            if odd_row != -1:
                return "Corrupt"
            odd_row = i + 1

    for j in range(n):
        col_sum: int = 0
        for i in range(n):
            col_sum += matrix[i][j]
        if col_sum % 2 != 0:
            if odd_col != -1:
                return "Corrupt"
            odd_col = j + 1

    if odd_row == -1 and odd_col == -1:
        return "OK"

    if odd_row != -1 and odd_col != -1:
        return f"Change bit ({odd_row},{odd_col})"

    return "Corrupt"


def create_matrix(string_input: str):
    lines: list[str] = dedent(string_input).strip().splitlines()
    n: int = int(lines[0])

    if not lines[1:]:
        raise ValueError("Empty matrix input")

    if len(lines) - 1 != n:
        raise ValueError("Number of rows doesn't match matrix size")

    matrix: list[list[str]] = []
    for line in lines[1:]:
        row: list[str] = [int(char) for char in line.split()]

        if len(row) != n:
            raise ValueError(f"Row length {len(row)} doesn't match matrix size {n}")

        matrix.append(row)

    return matrix


try:
    matrix = create_matrix("""
        4
        1 0 1 0
        0 0 1 0
        1 1 1 1
        0 1 0 1
        """)
    print(matrix)
    # This matrix is change bit (2,3)
    # From original matrix example change (1,2) to 0 to get ok matrix
    # From original matrix example change (3,2) to 1 to get corrupt matrix

    result: str = check_parity(matrix)
    print(result)
except ValueError as e:
    print(f"Error: {e}")
