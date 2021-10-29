def countingSort(arr: list[int]) -> list[int]:
    """[summary]

    Args:
        arr (list[int]): [description]

    Returns:
        list[int]: [description]
    """
    result_arr = [0] * 100
    for i in range(len(arr)):
        result_arr[arr[i]] += 1

    return result_arr


if __name__ == "__main__":
    print(countingSort([1, 1, 3, 2, 1]))
