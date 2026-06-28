class Solution:
    def subArrayExists(self,arr):
        seen = set()
        prefix = 0
        for num in arr:
            prefix += num
            if prefix == 0 or prefix in seen:
                return True
            seen.add(prefix)
        return False
        
