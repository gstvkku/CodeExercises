import java.util.HashSet;

class Solution {
    public int numberOfSpecialChars(String word) {
        char[] upperChars = word.toUpperCase().toCharArray();
        HashSet<Character> charSet = new HashSet<>();
        int result = 0;

        for (char c : upperChars) {
            charSet.add(c);
        }

        for (Character c : charSet) {
            if (word.contains(String.valueOf(c)) &&
                word.contains(String.valueOf(Character.toLowerCase(c)))) {
                result++;
            }
        }

        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        testar(solution, "aaAbcBC", 3);
        testar(solution, "abc", 0);
        testar(solution, "abBCab", 1);
        testar(solution, "Aaa", 1);
        testar(solution, "AaBbCc", 3);
    }

    private static void testar(Solution solution, String word, int esperado) {
        int resultado = solution.numberOfSpecialChars(word);

        System.out.println(
            "word = \"" + word + "\"" +
            " | esperado = " + esperado +
            " | resultado = " + resultado +
            " | " + (resultado == esperado ? "PASSOU" : "FALHOU")
        );
    }
}