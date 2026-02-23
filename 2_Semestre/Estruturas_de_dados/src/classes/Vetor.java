package classes;

public class Vetor {

    private int[] vector;

    public Vetor(int[] vector) {
        this.vector = vector;
    }

    public int[] getVector() {
        return vector;
    }

    public void printElement() {
        for (int element : vector) {
            System.out.println(element);
        }
    }
}

