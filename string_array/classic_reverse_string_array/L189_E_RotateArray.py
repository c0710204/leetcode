class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #side case
        if len(nums) <= 1:
          return 
        if k == 0:
          return
          
        # init
        i = 0
        j = 0
        extra_space=[]
        
        # code
        k=k%len(nums)
        extra_space=nums[-k:]
        for i in range(len(nums)-1,k-1,-1):
          nums[i]=nums[i-k]
        for i in range(k):
          nums[i]=extra_space[i]
        print(nums) 
        return


if __name__=="__main__":
  solu=Solution()
  assert(solu.rotate([1,2,3,4,5,6,7],7))
  assert(solu.rotate([-1,-100,3,99],2))
  assert(solu.rotate([],3))