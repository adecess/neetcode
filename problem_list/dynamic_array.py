class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * self.capacity 
        self.length = 0


    def get(self, i: int) -> int:
        if i < self.length:
            return self.arr[i]


    def set(self, i: int, n: int) -> None:
        if i < self.length:
            self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        
        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1


    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1

        return self.arr[self.length]
 

    def resize(self) -> None:
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity 

        # Copy elements to newArr
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity

