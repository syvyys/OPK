def gcd(first_num: int, second_num: int) -> int:
    """
    Finds the greatest common divisor for two numbers (Euclidean algorithm).
    """
    first_abs = abs(first_num)
    second_abs = abs(second_num)
    while first_abs != 0 and second_abs != 0:
            if first_abs > second_abs:
                first_abs %= second_abs
            else:
                second_abs %= first_abs
    return first_abs + second_abs


def test():
    assert (gcd(1, 2) == 1)
    assert (gcd(1, -2) == 1)


def main():
    test()
    first_num = int(input("Введите первое число: "))
    second_num = int(input("Введите второе число: "))
    print(gcd(first_num, second_num))


if __name__ == "__main__":
    main()