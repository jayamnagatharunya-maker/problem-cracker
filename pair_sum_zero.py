class Solution:
    def getPairs(self, arr):
        seen = set()
        pairs = set()
        for num in arr:
            if -num in seen:
                pairs.add(tuple(sorted((num, -num))))
            seen.add(num)
        return [list(pair) for pair in sorted(pairs)]
