1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    #rotating for k times= rotating for k%n times
8    def rotateRight(self, head, k):
9        if not head or not head.next:
10            return head
11        temp=head
12        n=1
13        while temp.next:
14            temp=temp.next
15            n+=1
16        tail=temp
17        tail.next=head
18        new_tail=head
19        k=k%n
20        steps=n-k-1
21        for _ in range(steps):
22            new_tail=new_tail.next
23        new_head=new_tail.next
24        new_tail.next=None
25        return new_head
26           