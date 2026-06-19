class Solution:
    def findDifference(self, a, b):
        a1 = set(a)
        b1 = set(b)
        set1 = list(a1 - b1)
        set2 = list(b1 - a1)
        return [set1, set2]
