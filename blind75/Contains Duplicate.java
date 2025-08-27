class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> hs = new HashSet<>();

        for (int item : nums){
            if (hs.contains(item)){
                return true;
            } else {
                hs.add(item);
            }
        }

        return false;
    }
}