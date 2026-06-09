class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for c in s:
            if c not in parMap:
                stack.append(c)
            else:
                if stack and parMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False