#https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        non_rep_list = []
        non_rep_string = ""
        for i in range(len(s)): 
            if s[i] not in non_rep_string:
                non_rep_string += s[i]
            
            else:
                non_rep_list.append(non_rep_string)
                non_rep_string = ""
                non_rep_string += s[i]
                
        if non_rep_string not in non_rep_list:
            non_rep_list.append(non_rep_string)
            
        if len(non_rep_list) == 0:
            return len(non_rep_string)
        
        word_length_list = [len(i) for i in non_rep_list]
    
                
        print(non_rep_list)
        
        print(word_length_list)
        
        if len(word_length_list) > 0:
            return max(word_length_list)
        
        elif s == "":
            return 0
        
        return 1
        