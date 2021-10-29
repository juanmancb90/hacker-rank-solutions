def caesarCipher(s: str, k: int) -> str:
    """[summary]

    Args:
        s (str): [description]
        k (int): [description]

    Returns:
        str: [description]
    """
    alphabet = [chr(x) for x in range(97, 123)]
    k = k % len(alphabet)
    alphabet_rotated = alphabet[k:] + alphabet[:k]
    alph_dict = dict(zip(alphabet, alphabet_rotated))
    rst = ""

    for item in s:
        if item.isalpha():
            value = (
                alph_dict.get(item.lower())
                if item.islower()
                else alph_dict.get(item.lower()).upper()
            )
            rst += value
        else:
            rst += item

    return rst


if __name__ == "__main__":
    assert caesarCipher("159357lcfd", 98) == "159357fwzx"
