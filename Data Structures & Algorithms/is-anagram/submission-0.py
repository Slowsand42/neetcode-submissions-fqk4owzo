class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}

        for n in s:
            hashmap[n] = hashmap.get(n, 0) + 1
        
        for n in t:
            if n in hashmap and hashmap[n] > 0:
                hashmap[n] -= 1
            else:
                return False
        return True
