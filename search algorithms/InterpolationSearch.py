# interpolation search - improved binary search with O(log(log N))

def interpolation_search(arr: list[int], val: int) -> int:
    # array has to be sorted beforehand
    arr.sort()
    # algorythm
    first = 0
    last = len(arr) - 1
    while arr[first] <= val <= arr[last] and first <= last:
        probe = first + (last - first) * (val - arr[first]) // (arr[last] - arr[first])
        if arr[probe] < val:
            first = probe + 1
        elif arr[probe] > val:
            last = probe - 1
        else:
            return probe
    return -1


def test():
    arr = [-4, 1, 2, 6, 8, 10, 13, 15, 18, 52, 65, 85, 122, 555]
    for i in range(len(arr)):
        assert interpolation_search(arr, arr[i]) == i


if __name__ == "__main__":
    test()