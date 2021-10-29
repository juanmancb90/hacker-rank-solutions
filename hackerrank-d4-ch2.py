def get_sum(n: str) -> int:
    """[summary]

    Args:
        n (str): [description]

    Returns:
        int: [description]
    """
    return sum(int(x) for x in n)


def superDigit(n, k) -> int:
    """[summary]

    Args:
        n ([type]): [description]
        k ([type]): [description]

    Returns:
        int: [description]
    """
    sum = 0
    if len(n) == 1:
        return int(n)
    else:
        t = str(get_sum(n) * k)
        sum += superDigit(t, 1)
    return int(sum)


if __name__ == "__main__":
    print(superDigit("9875", 4))
