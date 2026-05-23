class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while(True):
            num = 0
            if n >= 10:
                while n > 0:
                    digit = n % 10
                    num += digit * digit
                    n //= 10
                n = num
            else:
                n = n * n
            
            if n == 1:
                return True
            if n in seen:
                return False
            
            seen.add(n)