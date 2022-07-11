package java.ds;

import java.util.Stack;

public class StackList {
    public static void stackList() {
        Stack<String> deckOfCards = new Stack<>();
        String card1 = "Jack : Diamonds";
        String card2 = "8 : Hearts";
        String card3 = "3 : Club";

        deckOfCards.push(card1);
        deckOfCards.push(card2);
        deckOfCards.push(card3);
        System.out.println(deckOfCards);

        String top = deckOfCards.peek();
        System.out.println(top);

        System.out.println(deckOfCards.size());

        while (!deckOfCards.empty()) {
            String removeItem = deckOfCards.pop();
            System.out.println("Removed " + removeItem);
        }
    }

    public static void main(String[] args) {
        stackList();
    }
}