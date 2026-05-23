class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        # Initialize empty linked list
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        # Check if index is valid
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        # Traverse to the required index
        for _ in range(index):
            curr = curr.next

        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)

        # If list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        # If list is empty
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def remove(self, index: int) -> bool:
        # Invalid index
        if index < 0 or index >= self.size:
            return False

        # Remove head node
        if index == 0:
            self.head = self.head.next

            # If list becomes empty
            if not self.head:
                self.tail = None

        else:
            curr = self.head

            # Traverse to node before target
            for _ in range(index - 1):
                curr = curr.next

            # If removing tail node
            if index == self.size - 1:
                self.tail = curr
                curr.next = None
            else:
                curr.next = curr.next.next

        self.size -= 1
        return True

    def getValues(self) -> list[int]:
        values = []
        curr = self.head

        # Traverse linked list
        while curr:
            values.append(curr.val)
            curr = curr.next

        return values