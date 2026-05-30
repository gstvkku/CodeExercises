public class Main {

    static class Solution {
        public int minElement(int[] nums) {
            int result = -1;

            for (int i : nums) {
                String intStr = String.valueOf(i);
                String[] strValues = intStr.split("");
                i = 0;

                for (String j : strValues)
                    i += Integer.parseInt(j);

                if (result == -1 || i < result)
                    result = i;
            }

            return result;
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.minElement(new int[]{10, 20, 30}));    // 1
        System.out.println(sol.minElement(new int[]{1, 2, 3}));       // 1
        System.out.println(sol.minElement(new int[]{999, 123, 456})); // 6
    }
}