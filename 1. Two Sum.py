class Solution(object):
    def twoSum(self, nums, target):
        
        dic = {}
        for i in range(len(nums)):
            n = nums[i]
            m = target - n
            if m in dic:
                return dic[m], i
            else:
                dic[n] = i