#first program of leetcode; Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            j=i+1
            for j in range(i+1,len(nums)):
                if i<j and i!=j and nums[i] + nums[j] == target:
                    return(i,j)
