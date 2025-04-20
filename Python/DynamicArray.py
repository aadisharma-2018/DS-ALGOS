class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        if (capacity > 0):
            self.myArr = [0] * capacity
        
    def get(self, i: int) -> int:
        return self.myArr[i]

    def set(self, i: int, n: int) -> None:
        self.myArr[i] = n

    def pushback(self, n: int) -> None:
        if (self.size == self.capacity):
            self.resize()
        self.myArr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.myArr[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        newArr = [0] * self.capacity
        for i in range (self.size):
            newArr[i] = self.myArr[i]
        self.myArr = newArr

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.capacity
