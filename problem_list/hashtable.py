class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.table = [None] * capacity


    def hash(self, key):
        return key % self.capacity


    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        while True:
            if self.table[index] == None:
                self.table[index] = Pair(key, value)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.resize()
                return
            elif self.table[index].key == key:
                self.table[index].value = value
                return
            
            index += 1
            index = index % self.capacity


    def get(self, key: int) -> int:
        index = self.hash(key)
    
        while self.table[index] != None:
            if self.table[index].key == key:
                return self.table[index].value
            index += 1
            index = index % self.capacity
        return -1
        

    def remove(self, key: int) -> bool:
        if self.get(key) == -1:
            return False
    
        index = self.hash(key)
        while True:
            if self.table[index].key == key:
                self.table[index] = None
                self.size -= 1
                return True
            index += 1
            index = index % self.capacity


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        newTable = []
        for i in range(self.capacity):
            newTable.append(None)

        oldTable = self.table
        self.table = newTable
        self.size = 0
        for pair in oldTable:
            if pair:
                self.insert(pair.key, pair.value)


