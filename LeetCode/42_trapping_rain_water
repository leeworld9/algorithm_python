import time
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # DP 사용 : https://dev-note-97.tistory.com/m/272
        to_right = height.copy()
        to_left = height.copy()
        h_len = len(height)
        water = 0

        for i in range(1, h_len):
            to_right[i] = max(height[i], to_right[i - 1])
            to_left[h_len - i - 1] = max(height[h_len - i - 1], to_left[h_len - i])

        for j in range(0, len(height)):
            water += min(to_right[j], to_left[j]) - height[j]
        return water


"""
sol = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
start = time.time()
print(sol.trap(height))
print("time : {t} sec".format(t=time.time()-start))
"""