class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for value in nums:
            count[value] += 1

        freqBuckets = [ [] for i in range(len(nums)+1)]
        for value, freq in count.items():
            freqBuckets[freq].append(value)

        res = []
        for freq in reversed(range(len(freqBuckets))):
            for value in freqBuckets[freq]:
                res.append(value)
                if len(res) == k:
                    return res