import time
import numpy as np
import matplotlib.pyplot as plt

import MergeSort
import BubbleSort
import HeapSort


def benchmark(sort):
    sizes = []
    times = []
    for i in range(7):
        j = 100 * i
        sizes.append(j)
    for j in sizes:
        arr = np.random.sample(j)
        t1 = time.perf_counter()
        sort(arr)
        t2 = time.perf_counter()
        times.append(t2 - t1)
    return times, sizes


def main():
    times_bs, sizes = benchmark(BubbleSort.bubble_sort)
    times_ms, sizes = benchmark(MergeSort.merge_sort)
    times_hs, sizes = benchmark(HeapSort.heap_sort)
    plt.figure(figsize=(10, 5))
    plt.title('benchmark')
    plt.xlabel('size')
    plt.ylabel('time, s')
    plt.plot(sizes, times_bs, label='bubble sort')
    plt.plot(sizes, times_ms, label='merge sort')
    plt.plot(sizes, times_hs, label='heap sort')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
