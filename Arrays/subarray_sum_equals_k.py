class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        prefix = 0
        count = 0
        for i in nums:
            prefix += i
            if prefix - k in d:
                count += d[prefix - k]
            if prefix in d:
                d[prefix] += 1
            else:
                d[prefix] = 1
        return count
