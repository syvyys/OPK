import RandomArray


def bubble_sort(arr: list) -> list:
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def test():
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([0, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5]
    assert bubble_sort([1, 10, 6, -5, 4, 3]) == [-5, 1, 3, 4, 6, 10]
    arr = RandomArray.random_array(100)
    assert bubble_sort(arr.copy()) == sorted(arr.copy())


if __name__ == "__main__":
    test()