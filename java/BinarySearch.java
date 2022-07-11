package java;

public class BinarySearch {
    int binarySearch(int[] a, int low, int high, int key) {
        while (low <= high) {
            int mid = (low + high) / 2;

            if (a[mid] < key) {
                low = mid + 1;
            } else if (a[mid] > key) {
                high = mid - 1;
            } else {
                System.out.println("Element found at " + mid + " value " + a[mid]);
                return mid;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        BinarySearch search = new BinarySearch();
        int a[] = { 1, 2, 3, 4, 5, 6, 7, 7 };
        int key = 7;
        int low = 0;
        int high = (a.length - 1);
        System.out.println(search.binarySearch(a, low, high, key));
    }
}
