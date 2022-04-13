import math
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(int(len(nums)/2)):
            result += nums[2*i]
            # 오름차순으로 정렬시에는 짝이되는 값 중에서 반드시 앞의 값이 뒤의 값보다 적다
            # 따라서 추가로 최소값을 구할 필요는 없음
        return result

    """
    파이썬 다운 방식 (단 한줄로 해결 가능)
    return sum(sorted(nums)[::2])
    """

"""
sol = Solution()
nums = [6,2,6,5,1,2]
print(sol.arrayPairSum(nums))
"""