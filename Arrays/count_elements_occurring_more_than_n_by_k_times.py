class Solution:
    def countOccurence(self,arr, k):
        n = len(arr)
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        count = 0
        for freq in d.values():
            if freq > n // k:
                count += 1
        return count
        
