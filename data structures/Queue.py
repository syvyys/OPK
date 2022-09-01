class Queue:
    def __init__(self, max_size: int):
        assert max_size > 0
        self.arr = [0] * max_size

        self.cur_size = 0
        self.max_size = max_size

        self.read_idx = 0
        self.write_idx = 0

    def __len__(self):
        return len(self.arr)

    def push(self, value) -> None:
        if self.cur_size + 1 <= self.max_size:
            self.arr[self.write_idx] = value
            self.cur_size += 1
            self.write_idx += 1
            self.write_idx %= self.max_size
        else:
            raise IndexError('Queue is full!')

    def pop(self) -> any:
        if self.cur_size - 1 >= 0:
            self.cur_size -= 1
            self.read_idx += 1
            return self.arr[self.read_idx - 1]
        else:
            raise IndexError('Queue is empty!')


def test():
    queue = Queue(3)
    assert queue.arr == [0, 0, 0]
    queue.push(1)
    assert queue.arr == [1, 0, 0]
    queue.push(2)
    assert queue.arr == [1, 2, 0]
    queue.push(3)
    assert queue.arr == [1, 2, 3]
    assert queue.pop() == 1
    assert queue.pop() == 2
    queue.push(0)
    assert queue.arr == [0, 2, 3]
    queue.push(5)
    assert queue.arr == [0, 5, 3]


if __name__ == "__main__":
    test()