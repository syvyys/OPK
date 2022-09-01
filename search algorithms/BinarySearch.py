# binary search - O(log N)

def binary_search(arr: list[int], val: int) -> int:
    # array has to be sorted beforehand
    arr.sort()
    # algorythm
    first = 0
    last = len(arr) - 1
    while first <= last:
        middle = first + (last - first) // 2
        if arr[middle] < val:
            first = middle + 1
        elif arr[middle] > val:
            last = middle - 1
        else:
            return middle
    return -1


def test():
    arr = [-4, 1, 2, 6, 8, 10, 13, 15, 18, 52, 65, 85, 122, 555]
    for i in range(len(arr)):
        assert binary_search(arr, arr[i]) == i


if __name__ == "__main__":
    test()