class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string containing just the characters '(', ')', '{', '}', 
        '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Note that an empty string is also considered valid.
        """
        # side case
        if s=="":
          return True
        if len(s)==1:
          return False
        
        # init
        stack=['' for x in range(len(s)+1)]

        i=0
        j=0
        stack[j]='#'
        j=j+1
        s=s+'#'

        #logic
        for i in range(len(s)):
          if j<0:
            return False
          if s[i]==')' and stack[j-1]=='(':
            j=j-1
            continue
          if s[i]==']' and stack[j-1]=='[':
            j=j-1
            continue
          if s[i]=='}' and stack[j-1]=='{':
            j=j-1
            continue
          if s[i]=='#' and stack[j-1]=='#':
            j=j-1
            continue
          if s[i]=='(' or s[i]=='{' or s[i]=='[':
            stack[j]=s[i]
            j=j+1
            continue
          return False
        return True
          

if __main__=="__name__":
  solu=Solution()
  assert(solu(""))
  assert(solu("()"))
  assert(solu("[]"))
  assert(solu("{}"))
  assert(solu("{[()]}"))
  assert(solu("{[()]}"))
  assert(not solu("{[("))
  assert(not solu("("))
  assert(not solu(")"))
  assert(not solu(")}]"))
