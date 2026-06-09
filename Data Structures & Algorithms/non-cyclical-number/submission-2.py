class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            n = self.sumOfSquares(n)

            if n in seen:
                return False
            
            seen.add(n)
        
        return True
    
    def sumOfSquares(self, n):
        res = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            res += digit
            n = n // 10
        
        return res