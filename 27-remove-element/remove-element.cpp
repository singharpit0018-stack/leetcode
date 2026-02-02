class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        std::sort(nums.begin(), nums.end());
        int i = 0;
        while (i < nums.size() && nums[i] != val) {
            i++;
        }
        if (i == nums.size()) {
            return i;
        }
        int j = i;
        while (j < nums.size() && nums[j] == val) {
            j++;
        }
        if (j == nums.size()) {
            return i;
        }
        while (j < nums.size()) {
            nums[i] = nums[j];
            i++;
            j++;
        }

        return i;
    }

};