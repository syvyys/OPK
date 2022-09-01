import RandomArray


def insertion_sort(arr: list) -> list:
    # start with the first element - this is our sorted part for now
    # then add one element to this part and sort it
    for step in range(1, len(arr)):
        # we will find place in our sorted part for this key
        key = arr[step]
        # compare key with each element on the left of it until an element smaller than it is found
        idx = step - 1
        while idx >= 0 and arr[idx] > key:
            arr[idx + 1] = arr[idx]
            idx -= 1
        # place key at after the element smaller than it
        arr[idx + 1] = key
    return arr


def test():
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]
    assert insertion_sort([0, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5]
    assert insertion_sort([4, 5, 8, 1, 10, -1]) == [-1, 1, 4, 5, 8, 10]

    arr = random_array(100)
    assert insertion_sort(arr.copy()) == sorted(arr.copy())


if __name__ == "__main__":
    test()