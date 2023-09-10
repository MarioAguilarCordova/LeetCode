from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printlist(self, list):

        itr = list

        while itr:

            print(list.val + " , ")

            itr = itr.next


def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = result = ListNode(0)

        while list1 and list2:
            
            if list1.val < list2.val:

                result.next = list1
                list1 = list1.next
            else:

                result.next = list2
                list2 = list2.next

            result = result.next

        result.next = list1 or list2

        return dummy.next


def main():

    list1 = ListNode(1,2)
    list2 = ListNode(1,3)

    answer = ListNode(0)

    answer = mergeTwoLists(list1,list2)

    answer.printlist()


main()

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy = result = ListNode(0)

        while list1 and list2:
            
            if list1.val < list2.val:

                result.next = list1
                list1 = list1.next
            else:

                result.next = list2
                list2 = list2.next

            result = result.next
        
        result.next = list1 or list2

        return dummy.next

            
            
        return result