package classes;

public class Recursivity {

    // Não é recomendado declarar variáveis dentro de funções recursivas pq
    // isso irá gastar muita memória sem necessidade, uma vez que a cada
    // nova chamada um novo espaço na memória será utilizado pela declaração.

    public static int recursiveSUM(int start, int end) {

        if (start > end) {
            return 0;
        }

        if (start == end) {
            return end;
        }

        return start + recursiveSUM((start + 1), end);
    }

    // A grande diferença entre as duas formas de recursividade é que uma
    // retorna um valor (primeira) que é obtido pelo uso da própria função,
    // enquanto a outra (segunda) trata-se de um procedimento que invoca ele
    // próprio, sem necessidade de um retorno para funcionar > acumulador como
    // parâmetro torna-se essencial.

    public static void taillessRecursiveSUM(int start, int end, int aux) {

        if (start > end) {
            System.out.println("Inválido");
            return;
        }

        if (start == end) {
            System.out.println(aux + start);
            return;
        }

        taillessRecursiveSUM((start + 1), end, (aux + start));
    }

}
