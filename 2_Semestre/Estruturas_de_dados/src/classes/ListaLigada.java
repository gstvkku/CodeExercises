package classes;

public class ListaLigada {

    static class No {
        int valor;
        No proximo;

        No(int valor) {
            this.valor = valor;
            this.proximo = null;
        }
    }

    static No inicio = null;

    public static void simularLista() {

        // Inserir: 43 no início, 89 no final, 55 na posição 2
        inicio = new No(43);
        No meio = new No(55);
        inicio.proximo = meio;
        No fim = new No(89);
        meio.proximo = fim;

        // Consultar início e fim
        System.out.println(inicio.valor);
        No atual = inicio;
        while (atual.proximo != null) {
            atual = atual.proximo;
        }
        System.out.println(atual.valor);

        // Mostrar a lista
        atual = inicio;
        System.out.println(atual.valor);
        while (atual.proximo != null) {
            atual = atual.proximo;
            System.out.println(atual.valor);
        }

        // Remover os valores: 55, 43, 7, 89 (nesta ordem)
        remover(55);
        remover(43);
        remover(7);
        remover(89);

    }

    public static void remover(int numero) {
        No atual = inicio;

        if (atual == null) {
            System.out.println("Lista vazia.");
            return;
        }

        if (numero == atual.valor) {
            inicio = inicio.proximo;
            if (inicio == null) System.out.println("Lista vazia.");
            return;
        }


        while (atual.proximo != null) {
            No anterior = atual;
            atual = atual.proximo;

            if (numero == atual.valor) {
                anterior.proximo = (atual.proximo != null) ? atual.proximo : null;
                if (inicio == null) System.out.println("Lista vazia.");
                return;
            }
        }

        System.out.println("Elemento não existe na lista ligada.");
    }
}
