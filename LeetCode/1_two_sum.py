from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums[i + 1:]:  # 같은 시간복잡도 라도 in 연산쪽이 훨씬 더 가볍고 빠르다.
                return [nums.index(n), nums[i + 1:].index(diff) + (i + 1)]


"""
sol = Solution()
nums = [2, 3, 1, 3]
target = 6
print(sol.twoSum(nums, target))
"""
