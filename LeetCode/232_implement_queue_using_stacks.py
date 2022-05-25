class MyQueue:
    input_stack = None
    tmp_stack = None
    peek_data = None

    # 서적의 해설에서는 인덱싱을 이용하는데, 스택에 인덱싱을 사용하는건 맞지 않다고 판단하여 사용하지 않음.
    # 다만, pop() 부분은 좀 더 리펙토링은 가능해보임.

    def __init__(self):
        self.input_stack = []
        self.tmp_stack = []

    def push(self, x: int) -> None:  # 요소 x를 큐 마지막에 삽입한다.
        if self.peek_data is None:
            self.peek_data = x
        self.input_stack.append(x)

    def pop(self) -> int:  # 큐 처음에 있는 요소를 제거한다.
        while len(self.input_stack) != 0:
            self.tmp_stack.append(self.input_stack.pop())
        pop_data = self.tmp_stack.pop()
        self.peek_data = None
        while len(self.tmp_stack) != 0:
            tmp = self.tmp_stack.pop()
            if self.peek_data is None:
                self.peek_data = tmp
            self.input_stack.append(tmp)
        return pop_data

    def peek(self) -> int:  # 큐 처음에 있는 요소를 조회한다
        return self.peek_data

    def empty(self) -> bool:
        if len(self.input_stack) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
# obj.push(2)
# print(obj.peek())
# print(obj.pop())
print(obj.pop())
print(obj.empty())
