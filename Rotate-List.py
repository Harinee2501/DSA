1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def rotateRight(self, head, k):
8        temp=head
9        count=0
10        while temp:
11            count+=1
12            temp=temp.next
13        if not head or not head.next:
14            return head
15        temp=head
16        for _ in range(k%count):
17            while temp.next.next:
18                temp=temp.next
19            temp.next.next=head
20            head=temp.next
21            temp.next=None
22            temp=head
23        return head
24           