# Time: O(n^2)
# Space: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for outerIdx in range(len(nums) - 1):
            for innerIdx in range(outerIdx + 1, len(nums)):
                if nums[outerIdx] + nums[innerIdx] == target:
                    return [outerIdx, innerIdx]