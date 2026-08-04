class DynamicArray:
    
    def __init__(self, capacity: int):
        # Initialize array capacity, current element size, and a static storage list
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        # Returns the element at index i (assumes valid index context per problem)
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # Overwrites the element at index i with n
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # If the array is full, double its capacity before adding the element
        if self.size == self.capacity:
            self.resize()
            
        # Insert the element at the next available position
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # Removes and returns the last element in the array
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        # Double the capacity allocation size
        self.capacity *= 2
        new_arr = [0] * self.capacity
        
        # Copy the elements from the old array into the new resized array
        for i in range(self.size):
            new_arr[i] = self.arr[i]
            
        self.arr = new_arr

    def getSize(self) -> int:
        # Returns the number of active elements in the array
        return self.size

    def getCapacity(self) -> int:
        # Returns the current total allocated capacity of the array
        return self.capacity