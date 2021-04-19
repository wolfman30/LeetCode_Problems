# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def addTwoNumbers(self, l1, l2):
            
        string = ''
        string2 = ''
        
        print(l1)
        print()
        
        def convert_to_list(linked_list):
            
            new_list = [linked_list.val]
            next_node = linked_list.next
            if next_node is not None:
                new_list.append(next_node.val)
            while next_node is not None:
                next_node = next_node.next
                if next_node is not None:
                    new_list.append(next_node.val)
                
            return new_list
                
        def convert_to_reversed_number(list_item):
            string = ""
            reversed_l = [str(i) for i in list_item[::-1]]
            for i in reversed_l:
                string += i
                
            return int(string)
        
        
        def convert_list_to_llist(list_item):
            '''
            Got this from https://stackoverflow.com/questions/31553576/converting-a-list-to-a-linked-list
            Follows the link_to_list() syntax
            '''
            
            if len(list_item) == 1:
                return ListNode(list_item[0])
            
            return ListNode(list_item[0], convert_list_to_llist(list_item[1:]))
                
        
        l1_list = convert_to_list(l1)
        l2_list = convert_to_list(l2)
        combo = convert_to_reversed_number(l1_list) + convert_to_reversed_number(l2_list)
        
        combo_string_list = [i for i in str(combo)]
        
        final_list = [int(i) for i in combo_string_list[::-1]]
        
        print(convert_list_to_llist(final_list))
        
        final_result = convert_list_to_llist(final_list)
        
        return final_result
            
    
    

        

        