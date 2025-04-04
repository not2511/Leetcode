# Two sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       keys={}
       for i,n in enumerate(nums):
        diff=target-n
        if diff in keys:
            return [keys[diff],i]
        keys[n]=i
