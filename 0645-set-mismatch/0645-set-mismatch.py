from collections import Counter

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        s = set(nums)

        dup = sum(nums) - sum(s)
        mis = sum(range(1, n + 1)) - sum(s)
        return [dup, mis]
        