package java.ds;

public class LinkedListTest {
    Node head;

    public void add(int data) {
        // LL is empty
        if (this.head == null) {
            this.head = new Node(data);
        } else {
            // LL is not empty
            Node nodeToAdd = new Node(data);
            nodeToAdd.next = this.head;
            this.head = nodeToAdd;
        }
    }

    public static void main(String[] args) {
        LinkedListTest myList = new LinkedListTest();
        myList.add(10);
        myList.add(100);
        System.out.println(myList.head.data);
        System.out.println(myList.head.next.data);
    }
}

class Node {
    int data;
    Node next;

    Node(int d) {
        this.data = d;
    }
}
