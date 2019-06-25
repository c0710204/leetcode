class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass
        # ksp
        i=0
        j=0
        now_bitmap=0
        max_length=-1
        #ksp search loop
        for i in range(len(s)):
           
            for j in range(i,len(s)):
                local_int=1 << (ord(s[j])-ord('a'))
                if now_bitmap & local_int >0:
                    if max_length < j-i:
                        max_length = j - i
                now_bitmap=now_bitmap & local_int
                print(now_bitmap)
        print(max_length)
        return max_length


if __name__=="__main__":
    solu=Solution()
    assert(solu.lengthOfLongestSubstring("abcabcbb")==3)
    assert(solu.lengthOfLongestSubstring("bbbbb")==1)
    assert(solu.lengthOfLongestSubstring("pwwkew")==3)