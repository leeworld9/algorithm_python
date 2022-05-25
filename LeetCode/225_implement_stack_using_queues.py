from queue import Queue


class MyStack:
    blank_queue = None
    exist_queue = None
    top_data = None

    # 조건에 맞게 어디까지나 queue 연산만 사용하였음. ( 인덱싱도 사용하지 않음 )
    # deque의 다양한 연산자를 사용하면은 쉽지만 문제의 의도는 그게 아닌거 같아서 queue 연산가지고만 진행하였음.

    def __init__(self):
        self.blank_queue = Queue()
        self.exist_queue = Queue()

    def push(self, x: int) -> None:
        self.top_data = x
        self.blank_queue.put(x)
        while not self.exist_queue.empty():
            self.blank_queue.put(self.exist_queue.get())
        self.blank_queue, self.exist_queue = self.exist_queue, self.blank_queue

    def pop(self) -> int:
        pop_data = self.exist_queue.get()
        self.top_data = None

        while not self.exist_queue.empty():
            tmp = self.exist_queue.get()
            if self.top_data is None:
                self.top_data = tmp
            self.blank_queue.put(tmp)
        self.blank_queue, self.exist_queue = self.exist_queue, self.blank_queue
        return pop_data

    def top(self) -> int:
        return self.top_data

    def empty(self) -> bool:
        return self.exist_queue.empty()


# stack = MyStack()
# stack.push(1)
# stack.push(2)
# print(stack.pop())  # return 2
# print(stack.top())  # return 2
# print(stack.pop())  # return 2
# print(stack.empty())  # return False
