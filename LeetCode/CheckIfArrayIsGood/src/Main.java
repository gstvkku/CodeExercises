import java.util.HashSet;

class Solution {

    public boolean isGood(int[] nums) {

        HashSet<Integer> set = new HashSet<>();
        int n = nums.length;
        int base = -1;
        boolean result = false;

        for (int i : nums) {
            boolean addAttempt = set.add(i);

            if (!addAttempt) {
                base = (base == -1) ? i : -2;
            }
        }

        if (base != -1 && base != -2) {
            result = true;

            for (int j = 1; j < n - 1; j++) {
                if (!set.contains(j)) {
                    result = false;
                }
            }
        }

        return result;
    }
}

public class Main {

    public static void main(String[] args) {

        Solution sol = new Solution();

        int[] nums1 = {1, 2, 3, 3};
        int[] nums2 = {1, 2, 2};
        int[] nums3 = {1, 2, 3, 4, 5, 5};
        int[] nums4 = {1, 1};

        System.out.println("Teste 1: " + sol.isGood(nums1));
        System.out.println("Teste 2: " + sol.isGood(nums2));
        System.out.println("Teste 3: " + sol.isGood(nums3));
        System.out.println("Teste 4: " + sol.isGood(nums4));
    }
}