def maxSubarraySum(arr):
    currsum = 0
    maxsum = arr[0]
    for val in arr:
        currsum += val
        maxsum = max(maxsum, currsum)
        if currsum < 0:
            currsum = 0
    return maxsum
