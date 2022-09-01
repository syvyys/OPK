def selection_sort(arr: list) -> list:
    for i in range(len(arr) - 1):
        min_idx = i
        for idx in range(i + 1, len(arr)):
            if arr[idx] < arr[min_idx]:
                min_idx = idx
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def test():
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
    assert selection_sort([0, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5]
    assert selection_sort([4, 5, 8, 1, 10, -1]) == [-1, 1, 4, 5, 8, 10]


if __name__ == "__main__":
    test()