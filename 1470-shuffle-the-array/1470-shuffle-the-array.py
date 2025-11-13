class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        new = []
        nums_1 = nums[:n]
        nums_2 = nums[n:]
        for i in range(n):
            new.append(nums_1[i])
            new.append(nums_2[i])
        return new
        