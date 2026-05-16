class LinkedList {
    // Inner Node class
    private static class Node {
        int val;
        Node next;
        
        Node(int val) {
            this.val = val;
            this.next = null;
        }
    }

    private Node head;
    private Node tail;
    private int size;

    // Initializes an empty linked list
    public LinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }
    
    // Returns the value of the ith node (0-indexed). If out of bounds, returns -1.
    public int get(int index) {
        if (index < 0 || index >= size) {
            return -1;
        }
        
        Node curr = head;
        for (int i = 0; i < index; i++) {
            curr = curr.next;
        }
        return curr.val;
    }
    
    // Inserts a node with val at the head of the list
    public void insertHead(int val) {
        Node newNode = new Node(val);
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            newNode.next = head;
            head = newNode;
        }
        size++;
    }
    
    // Inserts a node with val at the tail of the list
    public void insertTail(int val) {
        Node newNode = new Node(val);
        if (tail == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }
        size++;
    }
    
    // Removes the ith node (0-indexed). If out of bounds, returns false, otherwise true.
    public boolean remove(int index) {
        if (index < 0 || index >= size) {
            return false;
        }
        
        // Case 1: Removing the head node
        if (index == 0) {
            head = head.next;
            if (head == null) { // If the list becomes empty
                tail = null;
            }
        } else {
            // Traverse to the node right before the one we want to remove
            Node curr = head;
            for (int i = 0; i < index - 1; i++) {
                curr = curr.next;
            }
            
            // Bypass the target node
            curr.next = curr.next.next;
            
            // Case 2: If we removed the tail node, update the tail pointer
            if (index == size - 1) {
                tail = curr;
            }
        }
        
        size--;
        return true;
    }
    
    // Changed return type and initialization to use java.util.ArrayList explicitly
    public java.util.ArrayList<Integer> getValues() {
        java.util.ArrayList<Integer> values = new java.util.ArrayList<>();
        Node curr = head;
        while (curr != null) {
            values.add(curr.val);
            curr = curr.next;
        }
        return values;
    }
}