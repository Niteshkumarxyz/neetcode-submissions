class LinkedList {

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

    public LinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

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

    public boolean remove(int index) {
        if (index < 0 || index >= size) {
            return false;
        }

        if (index == 0) {
            head = head.next;
            if (head == null) {
                tail = null;
            }
            size--;
            return true;
        }

        Node curr = head;
        for (int i = 0; i < index - 1; i++) {
            curr = curr.next;
        }

        curr.next = curr.next.next;
        if (curr.next == null) {
            tail = curr;
        }
        size--;
        return true;
    }

    public java.util.List<Integer> getValues() {
        java.util.List<Integer> values = new java.util.ArrayList<>();
        Node curr = head;
        while (curr != null) {
            values.add(curr.val);
            curr = curr.next;
        }
        return values;
    }
}