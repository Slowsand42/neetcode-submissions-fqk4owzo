class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
        if n == 0:
            return 1
        
        tmp = x

        for i in range(abs(n) - 1):
            x *= tmp

        return x