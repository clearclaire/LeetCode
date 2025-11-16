class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        curr, mayb = 0, 0
        
        for i in nums:
            if i == 1:
                mayb += 1
                curr = max(mayb, curr)
            else:
                mayb = 0
        return curr