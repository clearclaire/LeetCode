class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        count_map = {}

        for i, num in enumerate(sorted_nums):
            # 같은 숫자일 경우, 처음 등장한 인덱스만 저장
            if num not in count_map:
                count_map[num] = i
        return [count_map[num] for num in nums]

        # ans = []

        # for i in range(len(nums)):
        #     temp = 0
        #     for j in range(len(nums)):
        #         if nums[i] > nums[j]:
        #             temp += 1
        #     ans.append(temp)
        # return ans
    
        