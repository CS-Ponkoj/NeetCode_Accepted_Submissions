class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list=[]
        for i in range(len(strs)):
            # if strs[i] not in list:
            if any(strs[i] in sublist for sublist in list):
                continue
            else:
                temp_list= []
                temp_list.append(strs[i]) 
                for j in range(i+1,len(strs)):
                    if sorted(strs[i]) == sorted(strs[j]):
                        temp_list.append(strs[j])
                list.append(temp_list)

        return list

                
