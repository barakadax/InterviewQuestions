# Time O(Log N) | Space O(Log N)
def colName(n: int) -> str:
    res: list[str] = []

    while n > 0:
        rem: int = n % 26

        if rem == 0:
            res.append('Z')
            n = (n // 26) - 1

        else:
            res.append(chr((rem - 1) + ord('A')))
            n //= 26

    return ''.join(reversed(res))

n = 108
print(colName(n)) ## DD
