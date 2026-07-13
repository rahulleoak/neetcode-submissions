class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)

        for s in strs:

            charCount = [0] * 26

            for c in s:
                charCount[ord(c) - ord('a')] += 1
            

            key = tuple(charCount)
            anaMap[key].append(s)
        

        return list(anaMap.values())
    


