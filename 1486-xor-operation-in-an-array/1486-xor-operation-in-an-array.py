class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = 0
        for i in range(start, start + 2 * n, 2):
            nums ^= i
        return nums
        