package java.ds;

import java.util.LinkedList;

public class Linked {
  public static void linkedList() {
    LinkedList<String> students = new LinkedList<>();

    students.add("Prakash");
    students.add("Bishal");
    students.add("Anish");
    students.add("Tylor");
    students.add("Kevin");

    students.addFirst("Hari");
    students.addLast("Gita");
    students.add(3, "Kali");

    System.out.println(students);
    String firstStudents = students.getFirst();
    System.out.println("First Student: " + firstStudents);
    String lastStudents = students.getLast();
    System.out.println("Last Student: " + lastStudents);

    String getName = students.get(1);
    System.out.println("At index 1: " + getName);

    int i = students.indexOf("Prakash");
    System.out.println("Index of Prakash: " + i);

    students.removeFirst();
    students.removeLast();
    students.remove("Kali");
    students.remove(4);
    System.out.println(students);

    boolean hasPrakash = students.contains("Prakash");
    System.out.println(hasPrakash);

    students.clear();
    System.out.println(students);

  }

  public static void main(String[] args) {
    linkedList();
  }
}
