class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> j_index_map;
        for (int i = 0; i < nums.size(); i++) {
            int difference = target - nums[i];
            if (j_index_map.count(difference) != 0 && j_index_map[difference] != i) {
                return { i, j_index_map[difference]};
            }

            if (i > 1) {
                continue;
            }

            for (int j = 0; j < nums.size(); j++) { 
                if (difference == nums[j] && j != i) {
                    return { i, j };
                }

                j_index_map[nums[j]] = j;
            }
        }
    }
};
