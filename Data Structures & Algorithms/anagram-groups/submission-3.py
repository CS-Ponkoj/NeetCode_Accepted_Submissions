class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list=[]
        for i in range(len(strs)):
            # if strs[i] not in list:
            if any(strs[i] in sublist for sublist in list): # check if the string is already in the list/sublist or not
                continue    # if the string is already in the list, continue the loop
            else:
                temp_list= []
                temp_list.append(strs[i]) # append the string into a temporary list
                for j in range(i+1,len(strs)):
                    if sorted(strs[i]) == sorted(strs[j]): # check if angram or not
                        temp_list.append(strs[j]) # if it is angram, append the string to the emporary list
                list.append(temp_list) # append the temporary list into the final list

        return list

                
