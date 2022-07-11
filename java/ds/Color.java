package java.ds;

import java.util.List;
import java.util.ArrayList;

public class Color {
    public static void main(String[] args) {
        List<String> color = new ArrayList<>();
        color.add("red");
        color.add("blue");
        color.add("white");
        for (int i = 0; i < color.size(); i++) {
            System.out.println(color.get(i));
        }

        String[] colors = new String[3];
        colors[0] = "Red";
        colors[1] = "Blue";
        colors[2] = "White";
        for (int i = 0; i < colors.length; i++) {
            System.out.println(colors[i]);
        }
    }
}
