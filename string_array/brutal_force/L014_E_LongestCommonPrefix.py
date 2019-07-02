class Solution:
    def longestCommonPrefix(self, strs) -> str:
        """
        strs: List[str]
        Write a function to find the longest common prefix string amongst an
        array of strings.

        If there is no common prefix, return an empty string "".
        """
        # boundary condition
        if len(strs)==0:
          return ""
        if len(strs)==1:
          return strs[0]

        #init
        i=0
        j=0

        max_result_length=len(strs[0])
        result_length=0

        #code
        for i in range(1,len(strs)):
          max_result_length=min(max_result_length,len(strs[i]))

        if max_result_length==0:
          return ""

        result_length=max_result_length
        
        for i in range(max_result_length):
          for j in range(1,len(strs)):
            if strs[j][i]!=strs[0][i]:
              result_length=i
              break
          if result_length!=max_result_length:
            break

        return strs[0][:result_length]


if __name__=="__main__":
  solu=Solution()
  assert(solu.longestCommonPrefix(["flower","flow","flight"])=="fl")
  assert(solu.longestCommonPrefix(["dog","racecar","car"])=="")