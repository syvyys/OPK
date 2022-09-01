def heapify(arr: list, heap_size: int, root_index: int):
    parent = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    if left < heap_size and arr[left] > arr[parent]:
        parent = left

    if right < heap_size and arr[right] > arr[parent]:
        parent = right

    if parent != root_index:
        arr[root_index], arr[parent] = arr[parent], arr[root_index]
        heapify(arr, heap_size, parent)


def build_max_heap(arr: list):
    size = len(arr)
    for i in range(size, -1, -1):
        heapify(arr, size, i)


def heap_sort(arr: list) -> list:
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


def test():
    arr = RandomArray.random_array(10)
    assert heap_sort(arr.copy()) == sorted(arr.copy())


if __name__ == "__main__":
    test()