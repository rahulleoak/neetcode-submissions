class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtracking(idx, path):
            nonlocal res

            xor = 0
            for num in path:
                xor ^= num
            res += xor

            for i in range(idx, len(nums)):
                path.append(nums[i])

                backtracking(i + 1, path)

                path.pop()
            
        backtracking(0, [])
        return res
        