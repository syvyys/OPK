def min_max(arr: list[float]) -> (float, float):
    min_value = arr[0]
    max_value = arr[0]
    for num in arr:
        if min_value > num:
            min_value = num
        if max_value < num:
            max_value = num
    return min_value, max_value


def test_min_max():
    assert (min_max([0, 1, 5, 10, -10, 9, 25, 0]) == (-10, 25))
    assert (min_max([0, 4, 5, 6, 222, 41, 21]) == (0, 222))


def average(arr: list[float]) -> float:
    aver = 0
    for num in arr:
        aver += num
    aver = aver / len(arr)
    return aver


def test_average():
    assert (average([0, 1, 5, 10, -10, 9, 25, 8]) == 6)
    assert (average([0, 4, 5, 6, 222, 41, 21, 5]) == 38)


def standard_deviation(arr: list[float]) -> int:
    aver = average(arr)
    sig = 0
    for num in arr:
        sig += (num - aver) ** 2
    sig = int((sig / len(arr)) ** (1 / 2)) # выводим тип int - это нужно для отладки
    return sig


def test_standard_deviation():
    assert (standard_deviation([0, 1, 5, 10, -10, 9, 25, 8]) == 9)
    assert (standard_deviation([0, 4, 5, 6, 222, 41, 21, 5]) == 70)


def bubble_sort(arr: list[float]) -> list[float]:
    sorted_arr = arr.copy()
    for i in range(len(sorted_arr) - 1):
        for j in range(len(sorted_arr) - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr


def test_bubble_sort():
    assert (bubble_sort([1, 0, 5, 10, -10, 9, 25, 8]) == [-10, 0, 1, 5, 8, 9, 10, 25])
    assert (bubble_sort([6, 4, 6, 222, 41, 21, 5]) == [4, 5, 6, 6, 21, 41, 222])


def median(arr: list[float]) -> int:
    sorted_arr = bubble_sort(arr)
    len_arr = len(sorted_arr)
    if len_arr % 2 == 0:
        med = (sorted_arr[int(len_arr / 2) - 1] + sorted_arr[int(len_arr / 2 + 1) - 1]) / 2
    else:
        med = (sorted_arr[int((len_arr + 1) / 2) - 1]) / 2
    med = int(med)
    return med


def test_median():
    assert (median([1, 0, 5, 10, -10, 9, 25, 8]) == 6)
    assert (median([6, 4, 6, 222, 41, 21, 5]) == 3)


def max_num_repeating(arr: list[float]) -> int:
    max_num = 1
    temp = 1

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            temp += 1
        elif temp > max_num:
            max_num = temp
            temp = 1

    if temp > max_num:
        max_num = temp
    return max_num


def test_max_num_repeating():
    assert (max_num_repeating([1, 2, 2, 2, 3, 3, 3, 3, 3]) == 5)
    assert (max_num_repeating([1, 2, 3, 4]) == 1)
    assert (max_num_repeating([1, 1, 1, 1]) == 4)
    assert (max_num_repeating([1, 0, 0, 1, 1]) == 2)


def max_num_non_decreasing(arr: list[float]) -> int:
    max_num = 1
    temp = 1

    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            temp += 1
        elif temp > max_num:
            max_num = temp
            temp = 1

    if temp > max_num:
        max_num = temp
    return max_num


def test_max_num_non_decreasing():
    assert (max_num_non_decreasing([1, 2, 2, 2, 3, 3, 3, 3, 3]) == 9)
    assert (max_num_non_decreasing([1, 2, 3, 0]) == 3)
    assert (max_num_non_decreasing([1, 1, 1, 1]) == 4)
    assert (max_num_non_decreasing([1, 0, 0, 1, 1]) == 4)


def specifics_array(arr: list[float]):
    """
    Function specifics_array displays the characteristics of numbers
    """
    min_num, max_num = min_max(arr)
    print("Максимальное число: " + str(min_num) + " и минимальное число: " + str(max_num))
    print("Среднее арифметическое чисел: " + str(average(arr)))
    print("Стандартное отклонение: " + str(standard_deviation(arr)))
    print("Медиана: " + str(median(arr)))
    print("Наибольшее количество одинаковых подряд идущих элементов: " + str(max_num_repeating(arr)))
    print("Макс. длина монотонного участка подряд идущих элементов: " + str(max_num_non_decreasing(arr)))


def main():
    test_min_max()
    test_median()
    test_average()
    test_bubble_sort()
    test_max_num_non_decreasing()
    test_max_num_repeating()
    test_standard_deviation()
    n = int(input("Введите количество чисел в массиве: "))
    arr = []
    print("Вводите числа с клавиатуры:")
    for i in range(n):
        arr.append(float(input("")))
    specifics_array(arr)


if __name__ == "__main__":
    main()
