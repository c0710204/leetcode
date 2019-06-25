class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        # init local vars
        i=0
        j=0
        now_map={}
        max_length=-1
        #search loop
        for i in range(len(s)):
            now_map={}
            for j in range(i,len(s)):
                # check map
                if not now_map.get(s[j],False):
                    if max_length < j-i+1:
                        max_length = j - i + 1
                else:
                    break
                # update in-loop map
                now_map[s[j]]=True
        return max_length


if __name__=="__main__":
    solu=Solution()
    assert(solu.lengthOfLongestSubstring("abcabcbb")==3)
    assert(solu.lengthOfLongestSubstring("bbbbb")==1)
    assert(solu.lengthOfLongestSubstring("pwwkew")==3)
    assert(solu.lengthOfLongestSubstring("")==0)
    assert(solu.lengthOfLongestSubstring(" ")==1)
    assert(solu.lengthOfLongestSubstring("  ")==1)
    assert(solu.lengthOfLongestSubstring("  a")==2)
    assert(solu.lengthOfLongestSubstring("  a ")==2)