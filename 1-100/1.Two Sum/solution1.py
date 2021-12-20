class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
#Runtime: 4000 ms, faster than 26.80% of Python3 online submissions for Two Sum.
#Memory Usage: 14.9 MB, less than 80.53% of Python3 online submissions for Two Sum.
