class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> set;
        for (auto num : nums) {
            auto ret = set.insert(num);
            if (!ret.second) {
                return true;
            }
        }
        return false;
    }
};
