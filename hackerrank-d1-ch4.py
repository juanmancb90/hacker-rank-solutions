def findMedian(arr: list) -> int:
    """[summary]

    Args:
        arr (list): [description]

    Returns:
        int: [description]
    """
    arr.sort()
    middle = len(arr) // 2
    a = arr[middle]
    b = arr[-middle - 1]
    return int((a + b) / 2)


def flippingMatrix(matrix: list[list[int]]) -> int:
    """[summary]

    Args:
        matrix (list[list[int]]): [description]

    Returns:
        int: [description]
    """
    n = len(matrix)
    s = []
    for i in range(n // 2):
        for j in range(n // 2):
            s.append(
                max(
                    matrix[i][j],
                    matrix[i][n - j - 1],
                    matrix[n - i - 1][j],
                    matrix[n - i - 1][n - j - 1],
                )
            )
    return sum(s)


if __name__ == "__main__":
    print(findMedian([1, 2, 5, 6, 3, 8]))
    print(
        flippingMatrix(
            [
                [112, 42, 83, 119],
                [56, 125, 56, 49],
                [15, 78, 101, 43],
                [62, 98, 114, 108],
            ]
        )
    )
