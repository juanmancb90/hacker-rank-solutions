def diagonalDifference(arr: list[list], size: int) -> int:
    """[summary]

    Args:
        arr (list[list]): [description]
        size (int): [description]

    Returns:
        int: [description]
    """
    d1 = 0
    d2 = 0
    for i in range(size):
        for j in range(size):
            if i == j:
                d1 += arr[i][j]
            if (i + j) == size - 1:
                d2 += arr[i][j]
    rst = abs(d1 - d2)
    return rst


if __name__ == "__main__":
    mtx = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    print(diagonalDifference(mtx, 3))
