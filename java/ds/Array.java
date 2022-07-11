package java.ds;

import java.util.Arrays;

public class Array {
    public static void arrayPractice() {
        // declaring, allocating, and initializing an array

        String[] availablePets = { "cat", "dog", "rabbit" };
        String[] unavailablePets = { "bird", "hamster", "cock" };

        System.out.println(Arrays.toString(availablePets));
        System.out.println(Arrays.toString(unavailablePets));

        int indexAvailable = 2;
        int indexUnAvailable = 0;

        String availablePet = availablePets[indexAvailable];
        String unavailablePet = unavailablePets[indexUnAvailable];
        availablePets[indexAvailable] = availablePet;
        unavailablePets[indexUnAvailable] = unavailablePet;

        System.out.println(Arrays.toString(availablePets));
        System.out.println(Arrays.toString(unavailablePets));
    }

    public static void main(String[] args) {
        arrayPractice();
    }
}
