from typing import List


def get_sum(arr: list[int], index: int) -> int:
    """[summary]

    Args:
        arr (list[int]): [description]
        index (int): [description]

    Returns:
        int: [description]
    """
    tmp_arr = arr.copy()
    tmp_arr.pop(index)
    return sum(tmp_arr)


def miniMaxSum(arr: List[int]) -> str:
    """[summary]

    Args:
        arr (list[int]): [description]

    Returns:
        str: [description]
    """
    rst = [get_sum(arr, i) for i in range(len(arr))]
    print(f"{min(rst)} {max(rst)}")


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    miniMaxSum(arr)
