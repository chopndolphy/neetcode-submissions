class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = List[List[str]]
        string_map = {}
        for string in strs:
            chars = [0] * 26
            for i in range(len(string)):
                chars[ord(string[i]) - ord('a')] += 1
            key = ""
            for i in range(len(chars)):
                if chars[i] != 0:
                    key += str(chars[i])
                    key += chr(i + ord('a'))
            if key not in string_map:
                string_map[key] = [string]
            else:
                string_map[key].append(string)
        return string_map.values()
        
            

