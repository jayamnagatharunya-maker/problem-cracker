class Solution:
    def findDifference(self, a, b):
        return list(set(a) - set(b)), list(set(b) - set(a))
