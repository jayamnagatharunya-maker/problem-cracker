class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = nums[0]
        high = nums[0]
        while True:
            low = nums[low]
            high = nums[nums[high]]
            if low == high:
                break
        low = nums[0]
        while low != high:
            low = nums[low]
            high = nums[high]
        return low
