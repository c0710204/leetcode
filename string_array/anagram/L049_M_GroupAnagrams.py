class Solution:
    def groupAnagrams(self, strs):
        """
        groupAnagrams(self, strs: List[str]) -> List[List[str]]
        Given an array of strings, group anagrams together.

        Note:

        All inputs will be in lowercase.
        The order of your output does not matter.
        """
        # boundry condition
        if len(strs)==0:
          return []
        
        # init
        # char_dic:list[int]
        # key_list: dict[int->list[type(char_dic)]]
        # value_list: dict[int->list[list[str]]]
        # result_list: list[list[str]]
        key_list={}
        value_list={}
        char_dic=[0 for x in range(26)]
        result_list=[]
        i = 0
        j = 0
        found_key=False
        
        
        # code
        # find max_length to init list
        for i in range(len(strs)):
          key_list[len(strs[i])]=[]
          value_list[len(strs[i])]=[]
        
        for i in range(len(strs)):
          # local init
          found_key=False
          
          # loop
          
          char_dic=[0 for x in range(26)]
          
          for j in range(len(strs[i])):
            char_dic[ord(strs[i][j])-ord('a')]+=1 
          
          for j in range(len(key_list[len(strs[i])])):
            if key_list[len(strs[i])][j]==char_dic:
              found_key=True
              value_list[len(strs[i])][j].append(strs[i])
              break

          if not found_key:
            value_list[len(strs[i])].append([strs[i],])
            key_list[len(strs[i])].append(char_dic)
          
        for i in value_list.keys():
          for j in value_list[i]:
            result_list.append(j)

        return result_list

if __name__=="__main__":
  solu=Solution()
  
  assert(solu.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])==[
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
  )
  