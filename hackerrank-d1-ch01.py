def get_positive_numbers(number_list: list[int]) -> int:
    """[summary]

    Args:
        number_list (list[int]): [description]

    Returns:
        int: [description]
    """
    return len([i for i in number_list if i > 0])


def get_negative_numbers(number_list: list[int]) -> int:
    """[summary]

    Args:
        number_list (list[int]): [description]

    Returns:
        int: [description]
    """
    return len([i for i in number_list if i < 0])


def get_zero_numbers(number_list: list[int]) -> int:
    """[summary]

    Args:
        number_list (list[int]): [description]

    Returns:
        int: [description]
    """
    return len([i for i in number_list if i == 0])


def plusMinus(arr: list[int]) -> float:
    """[summary]

    Args:
        arr (list[int]): [description]

    Returns:
        float: [description]
    """
    n = len(arr)
    total_pos = get_positive_numbers(arr) / n
    total_neg = get_negative_numbers(arr) / n
    total_zer = get_zero_numbers(arr) / n
    return total_pos, total_neg, total_zer


if __name__ == "__main__":
    p, n, z = plusMinus([1, 2, 3, -1, -2, -3, 0, 0])
    print(f"{p: .6f}")
    print(f"{n: .6f}")
    print(f"{z: .6f}")
