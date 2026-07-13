class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement = {}

        for idx, val in enumerate(numbers):
            comp = target - val

            if comp in complement:
                return [complement[comp], idx + 1]
            
            complement[val] = idx + 1
        
            
