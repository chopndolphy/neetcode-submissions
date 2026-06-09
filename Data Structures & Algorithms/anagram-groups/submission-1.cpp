class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mapmap;
        for (auto str : strs) {
            vector<int> arr(26, 0);
            for (char c : str) {
                arr[c-'a']++;
            }
            string key;
            for (int i = 0; i < 26; i++) {
                key.append(to_string(arr[i]) + " ");
            }
            mapmap[key].push_back(str);
        }

        vector<vector<string>> anagramGroups;
        for (auto match : mapmap) {
            anagramGroups.push_back(match.second);
        }
        return anagramGroups;
    }
};
