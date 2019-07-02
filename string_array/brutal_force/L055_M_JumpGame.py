class Solution:
    def canJump(self, nums) -> bool:
        """
        nums: List[int]
        Given an array of non-negative integers, you are initially 
        positioned at the first index of the array.

        Each element in the array represents your maximum jump length at that 
        position.

        Determine if you are able to reach the last index.
        """
        #side case
        if len(nums)==0:
          return False
        
        if len(nums)==1:
          return True
        
        #init
        i=0
        j=0
        max_length=0

        #code
        for i in range(len(nums)):
          if max_length<i:
            return False
          max_length=max(max_length,i+nums[i])
        return True
if __name__=="__main__":
  solu=Solution()
  assert(solu.canJump([2,3,1,1,4]))
  assert(solu.canJump([2,5,0,0]))
  assert(not solu.canJump([3,2,1,0,4]))