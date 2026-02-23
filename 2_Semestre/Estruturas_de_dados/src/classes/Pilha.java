package classes;

public class Pilha {

    public static void simularPilha() {

        int[] myStack = new int[3];
        int peek = -1;

        // Empilhe: 5, 8, 4, 7
        if (peek < myStack.length - 1) myStack[++peek] = 5;
        if (peek < myStack.length - 1) myStack[++peek] = 8;
        if (peek < myStack.length - 1) myStack[++peek] = 4;
        if (peek < myStack.length - 1) myStack[++peek] = 7;

        if (peek == myStack.length - 1) {
            System.out.println("Pilha cheia!");
        }

        // Desempilhe duas vezes
        if (peek >= 0) peek--;
        if (peek >= 0) peek--;

        // Consulte o topo
        if (peek >= 0) {
            System.out.println(myStack[peek]);
        }

        // Desempilhe mais duas vezes
        if (peek >= 0) peek--;
        if (peek >= 0) peek--;

        if (peek == -1) {
            System.out.println("Pilha vazia!");
        }
    }
}
