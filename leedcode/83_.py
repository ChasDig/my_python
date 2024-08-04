#  https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        heads = dict()

        while head is not None:
            next_head = head.next_
            head.next_ = None

            if head.val not in heads.keys():
                heads[head.val] = head

            head = next_head

        if len(heads.keys()) == 1:
            return list(heads.values())[0]

        res = list()
        sorted_head_keys = sorted(heads.keys())
        for key_num in range(len(sorted_head_keys) - 1):
            current_head = heads[sorted_head_keys[key_num]]
            current_head.next_ = heads[sorted_head_keys[key_num + 1]]
            res.append(current_head)

        return res[0]


head_1 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
head_2 = ListNode(1, ListNode(1))

q = Solution().deleteDuplicates(head=head_1)

while q:
    print(q.val)
    q = q.next_
