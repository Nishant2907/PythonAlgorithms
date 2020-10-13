class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i=0
        j=0
        for x in s:
            i += ord(x)
        for x in t:
            j += ord(x)
        return chr(j-i)