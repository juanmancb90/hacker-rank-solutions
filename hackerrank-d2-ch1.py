from collections import Counter


def lonelyinteger(a: list[int]) -> int:
    """[summary]

    Args:
        a (list[int]): [description]

    Returns:
        int: [description]
    """
    counter_items = Counter(a)
    rst = dict(counter_items)
    for k, v in rst.items():
        if v == 1:
            return k


if __name__ == "__main__":
    v = lonelyinteger([1, 2, 3, 4, 3, 2, 1])
    print(v)
