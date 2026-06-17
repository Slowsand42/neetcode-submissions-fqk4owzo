class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenMap = {
                ")" : "(", 
                "}" : "{", 
                "]" : "["
                    }

        for c in s:
            if c not in parenMap:
                stack.append(c)
            else:
                if stack and parenMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
        return True if not stack else False