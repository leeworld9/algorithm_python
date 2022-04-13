from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 조건 : 나눗셈을 하지 않고 O(n)에 풀이하라.
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out

"""
sol = Solution()
nums = [1,2,3,4]
#nums = [-1,1,0,-3,3]
#nums = [-1,1,0,0,-3,3]
print(sol.productExceptSelf(nums))
"""

"""
[이해가 잘 안가서 디버깅 해본 내용]
ex) num[4]
    왼쪽  곱셈 : (1, 1*num[0], 1*num[0]*num[1], 1*num[0]*num[1]*num[2])
    오른쪽 곱셈 : (num[3]*num[2]*num[1]*1, num[3]*num[2]*1, num[3]*1, 1)
------------------------------------------------------------
result[0] = (num[3]*num[2]*num[1])
result[1] = (num[0]) * (num[3]*num[2])
result[2] = (num[0]*num[1]) * (num[3])
result[3] = (num[0]*num[1]*num[2])
"""