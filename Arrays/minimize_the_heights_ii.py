class Solution:
    def getMinDiff(self, arr, k):
        arr.sort()
        n = len(arr)
        ans = arr[-1] - arr[0]
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            small = min(arr[0] + k, arr[i] - k)
            large = max(arr[i - 1] + k, arr[-1] - k)
            ans = min(ans, large - small)
        return ans
