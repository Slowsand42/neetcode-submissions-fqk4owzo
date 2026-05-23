class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        res = []

        for n in digits:
            num += str(n)
        
        num2 = int(num) + 1

        num3 = str(num2)

        for n in num3:
            res.append(int(n))
        
        return res