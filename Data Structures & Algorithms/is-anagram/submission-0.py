class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        original = sorted(s)
        compared = sorted(t)
        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            if (original[i] != compared[i]):
                return False
        
        return True