class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:
                length = 1
                x = num
                while x + 1 in s:
                    x += 1
                    length += 1
                longest = max(longest, length)
        return longest
