import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split() if word not in banned]

        # Counter 모듈 사용
        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫번째 인덱스리턴
        return counts.most_common(1)[0][0]

sol = Solution()
paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
print(sol.mostCommonWord(paragraph, banned))
