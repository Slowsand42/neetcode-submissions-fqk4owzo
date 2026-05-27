class Solution:
    def reverse(self, x: int) -> int:
        count = 0
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x > 0:
            res = res * 10 + (x % 10)
            x = x // 10

        tmp = res
        while tmp:
            tmp = tmp >> 1
            count += 1
        
        if count >= 32:
            print(count)
            return 0
        else:
            return res * sign