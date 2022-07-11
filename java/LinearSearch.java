package java;

public class LinearSearch {
    public void linearSearch(int[] a, int key) {
        if (a.length == 0) {
            System.out.println("Empty List");
        }
        for (int i = 0; i < a.length; i++) {
            if (key == a[i]) {
                System.out.println("Element found " + " Int position: " + i);
                break;
            } else {
                System.out.println("Not");
            }
        }
    }

    public static void main(String[] args) {
        LinearSearch linearSearch = new LinearSearch();
        int key = 7;
        int[] elements = { 4, 7, 9, 3, 6 };
        linearSearch.linearSearch(elements, key);
    }
}
