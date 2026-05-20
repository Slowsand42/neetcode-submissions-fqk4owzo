class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res


















        
        
        # using freq map and set

        # res = []

        # count = {}
        # for c in s:
        #     count[c] = 1 + count.get(c, 0)

        # remaining = set()
        # curLen = 0
        # for c in s:
        #     if c not in remaining:
        #         remaining.add(c)
        #     curLen += 1
        #     count[c] -= 1

        #     if count[c] == 0:
        #         remaining.remove(c)
        #         if len(remaining) == 0:
        #             res.append(curLen)
        #             curLen = 0

        # return res