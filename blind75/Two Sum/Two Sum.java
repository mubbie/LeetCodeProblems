class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> tracking = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (tracking.containsKey(diff)) {
                int[] output = {tracking.get(diff), i};
                return output;
            } else {
                tracking.put(nums[i], i);
            }
        }

        return new int[0];
    }
}
