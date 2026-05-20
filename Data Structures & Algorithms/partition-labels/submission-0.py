class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # use freq maps to track how many characters are in s
        # keep growing substring until freq maps are empty for each char in substring
        # add counter to res list after freq maps hit 0
        # repeat algo on new substrings until end of s
        res = []

        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)

        remaining = set()
        curLen = 0
        for i, c in enumerate(s):
            if c not in remaining:
                remaining.add(c)
            curLen += 1
            count[c] -= 1

            if count[c] == 0:
                remaining.remove(c)
                if len(remaining) == 0:
                    res.append(curLen)
                    curLen = 0

        return res