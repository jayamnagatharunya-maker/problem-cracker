class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[-1] - nums[0]
        for i in range(1, n):
            small = min(nums[0] + k, nums[i] - k)
            large = max(nums[i - 1] + k, nums[-1] - k)
            ans = min(ans, large - small)
        return ans
