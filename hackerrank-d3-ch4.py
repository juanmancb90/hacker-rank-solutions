def is_palindre(word: str) -> bool:
    """[summary]

    Args:
        word (str): [description]

    Returns:
        bool: [description]
    """
    t = len(word)

    for i in range(t // 2):
        if word[i] != word[t - i - 1]:
            return False

    return True


def palindromeIndex(s: str) -> int:
    """[summary]

    Args:
        s (str): [description]

    Returns:
        int: [description]
    """
    n = len(s)

    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            if i + 1 < n:
                return i if is_palindre(s[i + 1 : n - i]) else n - i - 1

    return -1


if __name__ == "__main__":
    print(palindromeIndex("aaab".lower()))
    print(palindromeIndex("baa".lower()))
    print(palindromeIndex("aaa".lower()))
