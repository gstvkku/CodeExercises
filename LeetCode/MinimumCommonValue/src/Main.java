class Solution {

    public int getCommon(int[] nums1, int[] nums2) {

        for (int i : nums1) {
            for (int j : nums2) {
                if (i == j) {
                    return i;
                }
            }
        }

        return -1;
    }
}

public class Main {

    public static void main(String[] args) {

        Solution solution = new Solution();

        // Teste 1
        int[] nums1a = {1, 2, 3};
        int[] nums2a = {2, 4};

        int result1 = solution.getCommon(nums1a, nums2a);

        System.out.println("Teste 1");
        System.out.println("Esperado: 2");
        System.out.println("Obtido: " + result1);

        System.out.println("----------------");

        // Teste 2
        int[] nums1b = {1, 2, 3, 6};
        int[] nums2b = {4, 5, 6};

        int result2 = solution.getCommon(nums1b, nums2b);

        System.out.println("Teste 2");
        System.out.println("Esperado: 6");
        System.out.println("Obtido: " + result2);

        System.out.println("----------------");

        // Teste 3
        int[] nums1c = {1, 3, 5};
        int[] nums2c = {2, 4, 6};

        int result3 = solution.getCommon(nums1c, nums2c);

        System.out.println("Teste 3");
        System.out.println("Esperado: -1");
        System.out.println("Obtido: " + result3);
    }
}