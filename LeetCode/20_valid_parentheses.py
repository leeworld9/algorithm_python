class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c not in dict:
                stack.append(c)
            else:
                if not stack or dict[c] != stack.pop():
                    return False
        return len(stack) == 0

sol = Solution()
s = "{[()]}"
#s = "]"
print(sol.isValid(s))