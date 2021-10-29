def findZigZagSequence(a: list[int], n: int) -> str:
    """[summary]

    Args:
        a (list[int]): [description]
        n (int): [description]

    Returns:
        str: [description]
    """
    a.sort()
    mid = int(((n + 1) / 2) - 1)
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st += 1
        ed -= 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=" ")


if __name__ == "__main__":
    findZigZagSequence([1, 2, 3, 4, 5, 6, 7], 7)
