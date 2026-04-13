class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = {}
        s2Count = {}

        # build s1 frequency map
        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1

        l = 0
        for r in range(len(s2)):
            # add current char to window
            s2Count[s2[r]] = s2Count.get(s2[r], 0) + 1

            # shrink window if it's too big
            if (r - l + 1) > len(s1):
                s2Count[s2[l]] -= 1
                if s2Count[s2[l]] == 0:
                    del s2Count[s2[l]]
                l += 1

            # check if counts match
            if s1Count == s2Count:
                return True

        return False