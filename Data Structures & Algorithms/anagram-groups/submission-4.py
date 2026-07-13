class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)
        
        for word in strs:
            charMap = [0] * 26

            for ch in word:
                charMap[ord(ch) - ord('a')] += 1
            
            anaMap[tuple(charMap)].append(word)
        

        return list(anaMap.values())
