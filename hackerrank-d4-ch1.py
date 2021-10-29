def gridChallenge(grid: list[str]) -> str:
    """[summary]

    Args:
        grid (list[str]): [description]

    Returns:
        str: [description]
    """
    mtx = [list(sorted(item)) for item in grid]
    rst = "YES"
    mtx_size, col_size = len(grid), len(mtx[0])

    for i in range(col_size):
        for j in range(1, mtx_size):
            if not mtx[j - 1][i] <= mtx[j][i]:
                rst = "NO"

    return rst


if __name__ == "__main__":
    print(gridChallenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]))
