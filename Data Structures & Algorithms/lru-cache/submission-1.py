class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cont = {}
        self.order = []

    def get(self, key: int) -> int:
        if key not in self.cont:
            return -1
        self.order.remove(key)
        self.order.append(key)

        return  self.cont[key] 

    def put(self, key: int, value: int) -> None:
        if key in self.cont:
            self.order.remove(key)
        elif len(self.order) >= self.capacity:
            old = self.order.pop(0)
            del self.cont[old]
        self.cont[key] = value
        self.order.append(key)