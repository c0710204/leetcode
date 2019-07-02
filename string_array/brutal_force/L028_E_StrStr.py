class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Implement strStr().

        Return the index of the first occurrence of needle in haystack, or -1 
        if needle is not part of haystack.
        """
        # side case
        if needle=="":
          return 0
        
        if haystack=="":
          return -1
        
        # init
        i = 0
        j = 0
        matched = True

        # code
        # KSP search
        for i in range(len(haystack)-len(needle)+1):
          matched = True

          for j in range(len(needle)):
            if haystack[i+j]!=needle[j]:
              matched = False
              break;

          if matched:
            return i
        return -1    




if __name__=="__main__":
  solu=Solution()
  assert(solu.strStr("","")==0)
  assert(solu.strStr("","111")==-1)
  assert(solu.strStr("abc","abc")==0)
  assert(solu.strStr("sabc","abc")==1)
  assert(solu.strStr("abcabc","abc")==0)
  assert(solu.strStr("abbabc","abc")==3)