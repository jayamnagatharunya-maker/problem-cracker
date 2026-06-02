class Solution:
    def getMinMax(self, arr):
            min = arr[0]
            max = arr[0]
            for element in arr:
                if element < min:
                    min = element
                if element > max:
                    max = element
            return [min, max]
