
class Solution:
    def reverseString(self, s) -> None:
        """
        Share
        Write a function that reverses a string. The input string is given as 
        an array of characters char[].

        Do not allocate extra space for another array, you must do this by modi
        fying the input array in-place with O(1) extra memory.

        You may assume all the characters consist of printable ascii characters.
        Do not return anything, modify s in-place instead.
        """
        #side case
        if len(s) <= 1:
          return
        #init
        s_length=len(s)
        i=0
        #code
        for i in range(int(s_length/2)):
          s[i],s[s_length-1-i]=s[s_length-1-i],s[i]
        return
        
if __name__=="__main__":
  solu=Solution()
  s = ["h","e","l","l","o"]
  solu.reverseString(s)
  assert(s == ["o","l","l","e","h"])

