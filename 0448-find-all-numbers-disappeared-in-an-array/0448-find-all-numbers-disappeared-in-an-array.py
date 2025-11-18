class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        out = [i for i in range(1, len(nums)+1) if i not in s]
        
        return out
        