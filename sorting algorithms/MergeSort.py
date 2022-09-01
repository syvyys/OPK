import RandomArray


def merge_sort(arr: list) -> list:
    if len(arr) > 1:
        mid_idx = len(arr) // 2
        left = arr[:mid_idx]
        right = arr[mid_idx:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)
    return arr


def merge(left: list, right: list, arr: list) -> None:
    left_idx, right_idx, arr_idx = 0, 0, 0

    # merge two arrays until at least one of them is fully merged
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            arr[arr_idx] = left[left_idx]
            left_idx += 1
        else:
            arr[arr_idx] = right[right_idx]
            right_idx += 1
        arr_idx += 1

    # then put leftovers in the array
    while left_idx < len(left):
        arr[arr_idx] = left[left_idx]
        left_idx += 1
        arr_idx += 1

    while right_idx < len(right):
        arr[arr_idx] = right[right_idx]
        right_idx += 1
        arr_idx += 1


def test():
    arr = RandomArray.random_array(100)
    assert merge_sort(arr.copy()) == sorted(arr.copy())


if __name__ == "__main__":
    test()