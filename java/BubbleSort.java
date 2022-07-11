package java;

public class BubbleSort {
    public void sort(int[] a) {
        for (int i = 0; i < a.length; i++) {
            int minVal = minimumValue(a, i);
            swap(a, minVal, i);
        }
        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
        }
    }

    public int minimumValue(int[] a, int form) {
        int minVal = form;
        for (int i = form + 1; i < a.length; i++) {
            if (a[i] < a[minVal]) {
                minVal = 1;
            }
        }
        return minVal;
    }

    public void swap(int[] a, int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    public static void main(String[] args) {
        BubbleSort sort = new BubbleSort();
        int[] b = { 5, 11, 17, 9, 12 };
        System.out.println(b);
        sort.sort(b);
    }
}
