from typing import Union


def minimumBribes(q: list[int]) -> Union[int, str]:
    """[summary]

    Args:
        q (list[int]): [description]

    Returns:
        Union[int, str]: [description]
    """
    swap_counter = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] != i + 1:
            if q[i - 1] == i + 1:
                swap_counter += 1
                q[i], q[i - 1] = q[i - 1], q[i]
            elif q[i - 2] == i + 1:
                swap_counter += 2
                t = q[i - 2]
                q[i - 2], q[i - 1], q[i] = q[i - 1], q[i], t
            else:
                return "Too chaotic"
        else:
            continue

    return swap_counter


if __name__ == "__main__":
    print(minimumBribes([2, 1, 5, 3, 4]))
