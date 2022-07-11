package java.ds;

import java.util.LinkedList;
import java.util.Queue;

public class QueueList {
    public static void queueList() {
        Queue<String> queue = new LinkedList<>();

        queue.add("Prakash");
        queue.add("Bishal");
        queue.add("Hari");
        queue.add("Shyam");

        System.out.println(queue);

        String nextInqueue = queue.peek();
        System.out.println("Next up! " + nextInqueue);

        // for (int i = 0; i < queue.size() ;i++ ) {
        // queue.remove();
        // System.out.println(queue);
        // }

        String recentlyRemoved = queue.remove();
        System.out.println(recentlyRemoved);
        System.out.println(queue);
    }

    public static void main(String[] args) {
        queueList();
    }
}
