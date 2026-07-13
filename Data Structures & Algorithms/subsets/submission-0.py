class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def subset(start, path):
            res.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                subset(i+1, path)
                path.pop()

        subset(0, path)
        return res