import java.util.HashSet;

class Solution {
    public int numberOfSpecialChars(String word) {
        int result = 0;

        char[] upperChars = word.toUpperCase().toCharArray();
        HashSet<Character> charSet = new HashSet<>();

        for (char c : upperChars) {
            charSet.add(c);
        }

        String upper;
        String lower;
        int firstUpper;
        int lastLower;

        for (Character c : charSet) {
            upper = String.valueOf(c);
            lower = String.valueOf(Character.toLowerCase(c));

            if (word.contains(upper) && word.contains(lower)) {
                firstUpper = word.indexOf(upper);
                lastLower = word.lastIndexOf(lower);
                if (lastLower < firstUpper) result++;
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
        testar(solution, "AbBCab", 0);
        testar(solution, "AaBbCc", 0);
        testar(solution, "abcABC", 3);
        testar(solution, "aA", 1);
        testar(solution, "Aaa", 0);
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