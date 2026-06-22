class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0
        if arr[0] == 0:
            return -1
        jumps = 0
        left = 0
        right = 0
        while right < n - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + arr[i])
            if farthest == right:
                return -1
            left = right + 1
            right = farthest
            jumps += 1
        return jumps
