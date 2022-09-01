import random


def random_array(n: int) -> list[int]:
    arr = []
    for _ in range(n):
        arr.append(random.randint(0, 1000))
    return arr