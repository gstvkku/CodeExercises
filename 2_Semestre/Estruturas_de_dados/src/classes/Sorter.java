package classes;

public class Sorter {

    public static void bubbleSort(int[] array) {
        int n = array.length;
        boolean trocou;

        for (int i = 0; i < n - 1; i++) {
            trocou = false;

            for (int j = 0; j < n - 1 - i; j++) {
                if (array[j] > array[j + 1]) {
                    // troca os elementos
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                    trocou = true;
                }
            }

            // se não houve troca, o array já está ordenado
            if (!trocou) {
                break;
            }
        }

    }

    public static void quickSort(int[] array, int inicio, int fim) {
        if (inicio < fim) {
            int pivoIndex = particionar(array, inicio, fim);

            // Ordena os elementos antes e depois do pivô
            quickSort(array, inicio, pivoIndex - 1);
            quickSort(array, pivoIndex + 1, fim);
        }
    }

    // Função que organiza o array em torno do pivô
    private static int particionar(int[] array, int inicio, int fim) {
        int pivo = array[fim]; // escolhe o último elemento como pivô
        int i = inicio - 1;

        for (int j = inicio; j < fim; j++) {
            if (array[j] <= pivo) {
                i++;

                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }

        int temp = array[i + 1];
        array[i + 1] = array[fim];
        array[fim] = temp;

        return i + 1;
    }

    public static void mergeSort(int[] array, int inicio, int fim) {
        // condição de parada: 1 elemento
        if (inicio < fim) {
            int meio = (inicio + fim) / 2;

            // divide
            mergeSort(array, inicio, meio);
            mergeSort(array, meio + 1, fim);

            // conquista (merge)
            merge(array, inicio, meio, fim);
        }
    }

    private static void merge(int[] array, int inicio, int meio, int fim) {
        int[] temp = new int[fim - inicio + 1];

        int i = inicio;     // ponteiro da esquerda
        int j = meio + 1;   // ponteiro da direita
        int k = 0;          // ponteiro do array temporário

        // compara e ordena
        while (i <= meio && j <= fim) {
            if (array[i] <= array[j]) {
                temp[k++] = array[i++];
            } else {
                temp[k++] = array[j++];
            }
        }

        // sobra da esquerda
        while (i <= meio) {
            temp[k++] = array[i++];
        }

        // sobra da direita
        while (j <= fim) {
            temp[k++] = array[j++];
        }

        // copia de volta pro array original
        for (int x = 0; x < temp.length; x++) {
            array[inicio + x] = temp[x];
        }
    }

}
