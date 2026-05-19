class Solution {

    public boolean canReach(int[] arr, int start) {
        boolean[] visited = new boolean[arr.length];
        return dfs(arr, start, visited);
    }

    public boolean dfs(int[] arr, int index, boolean[] visited) {

        // índice inválido
        if (index < 0 || index >= arr.length) {
            return false;
        }

        // já visitado
        if (visited[index]) {
            return false;
        }

        // encontrou zero
        if (arr[index] == 0) {
            return true;
        }

        // marca como visitado
        visited[index] = true;

        // tenta direita OU esquerda
        return dfs(arr, index + arr[index], visited) ||
               dfs(arr, index - arr[index], visited);
    }
}

public class Main {

    public static void main(String[] args) {

        Solution solution = new Solution();

        int[] arr1 = {4, 2, 3, 0, 3, 1, 2};
        int start1 = 5;

        boolean result1 = solution.canReach(arr1, start1);

        System.out.println("Teste 1:");
        System.out.println("Resultado esperado: true");
        System.out.println("Resultado obtido: " + result1);

        System.out.println("-------------------");

        int[] arr2 = {3, 0, 2, 1, 2};
        int start2 = 2;

        boolean result2 = solution.canReach(arr2, start2);

        System.out.println("Teste 2:");
        System.out.println("Resultado esperado: false");
        System.out.println("Resultado obtido: " + result2);
    }
}