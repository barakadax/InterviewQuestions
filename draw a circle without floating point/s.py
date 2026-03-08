# Time O(N power 2) | Space O(1)
def drawCircle(r: int) -> None:
    diameter: int = 2 * r + 1

    for i in range(diameter):
        for j in range(diameter):
            x: int = i - r
            y: int = j - r

            if x * x + y * y <= r * r + 1:
                print("X", end = " ")
            else:
                print(" ", end = " ")

        print()

drawCircle(4)
