class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t , write a function to determine if t is an anagram of s.
        """
        # boundry cond
        
        # init
        i=0
        char_dic=[0 for x in range(26)]

        # code
        for i in range(len(s)):
          char_dic[ord(s[i])-ord('a')]+=1
        for i in range(len(t)):
          char_dic[ord(t[i])-ord('a')]-=1

        for i in range(26):
          if char_dic[i]!=0:
            return False
        return True

if __name__=="__main__":
  solu=Solution()
  assert(solu.isAnagram("a","a"))
  assert(solu.isAnagram("",""))
  assert(not solu.isAnagram("","a"))         
