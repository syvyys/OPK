def fibonacci_number(n: int) -> int:
    """
    Counts Nth Fibonacci number (with cycle)
    """
    if n <= 0:
        return 0
    else:
        index = 0
        first = second = 1
        while index <= n - 3:
            first, second = second, first + second
            index += 1
        return second


def fibonacci_recursion(n: int) -> int:
    """
    Counts Nth Fibonacci number (with recursion)
    """
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


def factorial(n: int) -> int:
    """
    Counts Nth factorial (with recursion)
    """
    if n > 0:
        return factorial(n-1) * n
    else:
        return 1


def test():
    assert fibonacci_number(0) == 0
    assert fibonacci_recursion(0) == 0
    assert fibonacci_number(1) == 1
    assert fibonacci_recursion(1) == 1
    assert fibonacci_number(2) == 1
    assert fibonacci_recursion(2) == 1
    assert fibonacci_number(3) == 2
    assert fibonacci_recursion(3) == 2
    assert fibonacci_number(4) == 3
    assert fibonacci_recursion(4) == 3
    assert fibonacci_number(5) == 5
    assert fibonacci_recursion(5) == 5


def main():
    test()
    n = int(input("Input n: "))
    print(fibonacci_number(n))
    print(fibonacci_recursion(n))
    print(factorial(n))


if __name__ == "__main__":
    main()
