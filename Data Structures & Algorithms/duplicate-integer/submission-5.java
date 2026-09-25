class Solution {
    public boolean hasDuplicate(int[] nums) {
        // use hashset for unique values

        HashSet<Integer> numSet = new HashSet<>();

        for (int i = 0; i < nums.length; ++i) {
            if (numSet.contains(nums[i])) {
                return true;
            }
            numSet.add(nums[i]);
        }
        return false;
    }
}