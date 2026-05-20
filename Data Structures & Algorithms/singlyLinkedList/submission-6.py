class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        # Initializes an empty linked list
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        # If the index is out of bounds, return -1
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        # FIX: Explicitly initialize new_node before using it
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove(self, index: int) -> bool:
        # If the index is out of bounds, return False
        if index < 0 or index >= self.size:
            return False
        
        # Case 1: Removing the head node
        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
        # Case 2: Removing a middle or tail node
        else:
            curr = self.head
            # Travel to the node right BEFORE the target node
            for _ in range(index - 1):
                curr = curr.next
            
            # FIX: Use an if-else structure to cleanly separate tail vs middle deletion
            if index == self.size - 1:
                self.tail = curr
                curr.next = None
            else:
                curr.next = curr.next.next
                
        self.size -= 1
        return True

    def getValues(self) -> list[int]:
        # Return an array of all values ordered from head to tail
        values = []
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values