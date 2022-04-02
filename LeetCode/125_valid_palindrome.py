import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.lower()
        new_s = re.sub('[^a-z0-9]', '', new_s)  # 정규식으로 불필요한 문자 필터링
        return new_s == new_s[::-1] # 슬라이싱


"""
sol = Solution()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))
"""