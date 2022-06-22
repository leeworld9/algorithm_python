class MyHashMap:
    h_dict = None

    def __init__(self):
        self.h_dict = {}

    def put(self, key: int, value: int) -> None:
        self.h_dict[key] = value

    def get(self, key: int) -> int:
        if key in self.h_dict:
            return self.h_dict[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.h_dict:
            del self.h_dict[key]

