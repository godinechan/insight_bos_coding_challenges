
"""
Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
"""

#constructor for a Node of singly linked list
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def oddEvenList_Helper(head):

    # head_odd keeps track of the last consecutive odd from the left
    head_odd = head
    
    # head_even_1 and head_even_2 keep track of the first and last consecutive evens from the left
    head_even_1 = head.next
    head_even_2 = head.next
    
    # iterate until either head_even_2 or head_even_2.next = None (no more odds)
    while head_even_2 and head_even_2.next:
        
        # move head_even_2.next (which is an odd) to in between head_odd and head_even_1, and increment head_odd
        head_odd.next = head_even_2.next
        head_odd = head_odd.next
        
        # increment head_even_2 after updating its link (head_odd.next still points to the next even)
        head_even_2.next = head_odd.next
        head_even_2 = head_even_2.next
        
        # update the link of the last consecutive odd to the start of the evens
        head_odd.next = head_even_1
        
    return head


#DO NOT CHANGE THIS FUNCTION
def oddEvenList(head):
    return oddEvenList_Helper(head)


#test case
def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head =  oddEvenList(head)
    print ("Expected result: 1, 3, 5, 2, 4")
    print ("Your result is {}, {}, {}, {}, {}".format(head.data, head.next.data, head.next.next.data, head.next.next.next.data, head.next.next.next.next.data))

if __name__ == "__main__":
    main()