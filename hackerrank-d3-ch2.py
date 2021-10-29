def towerBreakers(n: int, m: int) -> int:
    """[summary]

    Args:
        n (int): [description]
        m (int): [description]

    Returns:
        int: [description]
    """
    if n % 2 == 0 or m == 1:
        return 2
    else:
        return 1


if __name__ == "__main__":
    print(towerBreakers(100000, 1))
    print(towerBreakers(100001, 1))
    print(towerBreakers(658843, 684118))
    print(towerBreakers(70585, 944105))
    print(towerBreakers(642564, 944465))
    print(towerBreakers(26518, 867395))
