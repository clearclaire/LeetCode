class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # new = nums[:max(nums).index()]
        diff = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if ((nums[j] - nums[i]) >= 1) & ((nums[j] - nums[i]) > diff) :
                    diff = nums[j] - nums[i]
        if diff <= 0:
            return -1
        return diff

        