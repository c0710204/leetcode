class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Given an input string, reverse the string word by word.
        Follow up:
        For C programmers, try to solve it in-place in O(1) extra space.
        """
        # side case
        i = 0
        flag = True
        for i in range(len(s)):
          if s[i] == " ":
            flag = False
        if flag:
          return s
        # init
        word_end = len(s)
        new_str = ""
        i=0
        j=0
        # code
        for i in range(len(s)-1,-1,-1):
          if s[i]==" ":
            #do copy
            for j  in range(i+1,word_end):
              new_str=new_str+s[j]
            if i+1<word_end :
              new_str=new_str+' '
            word_end=i
        # do last copy
        for j  in range(0,word_end):
          new_str=new_str+s[j]
        word_end=i
        if len(new_str)>0 and new_str[-1]==' ':
          new_str=new_str[:-1]
        return new_str
        
          

if __name__=="__main__":
  solu=Solution()
  assert(solu.reverseWords("the sky is blue")=="blue is sky the")
  assert(solu.reverseWords("  hello world!  ")=="world! hello")
  assert(solu.reverseWords("a good   example")=="example good a")  