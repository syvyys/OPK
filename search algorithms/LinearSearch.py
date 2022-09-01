# linear search - O(N)

def linear_search(arr: list[int], val: int) -> int:
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1


def test():
    arr = [-4, 1, 2, 6, 8, 10, 13, 15, 18, 52, 65, 85, 122, 555]
    for i in range(len(arr)):
        assert linear_search(arr, arr[i]) == i


if __name__ == "__main__":
    test()