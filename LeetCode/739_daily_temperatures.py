from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            # 현재 온도가 스택값 보다 높다면 정답처리
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                # 디버기용
                #print(f"answer[{last}] = {i} - {last}")
                answer[last] = i - last
            stack.append(i)
        # 디버기용
        #print("stack : ", stack)
        return answer


# sol = Solution()
# temperatures = [73,74,75,71,69,72,76,73]
# print(sol.dailyTemperatures(temperatures))