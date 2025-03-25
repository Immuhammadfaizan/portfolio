from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total_outer_iters = 0
        total_inner_iters = 0
        
        for i in range(len(nums)):
            total_outer_iters += 1
            for j in range(i + 1, len(nums)):
                total_inner_iters += 1
                if nums[i] + nums[j] == target:
                    return [i, j]
        print(f"Total outer iterations: {total_outer_iters}")
        print(f"Total inner iterations: {total_inner_iters}")
        return []

nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)
print(f"Result: {result}")
