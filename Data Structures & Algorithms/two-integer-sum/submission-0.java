class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] solution = new int[2];
        boolean found = false;
        for (int i = 0; i < nums.length; i++) {
            if (found == true) {
                break;
            }
            for (int j = i+1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    solution[0] = i;
                    solution[1] = j;
                    found = true;
                    break;
                }
                else {
                    continue;
                }
            }
        }
        return solution;
    }
}
