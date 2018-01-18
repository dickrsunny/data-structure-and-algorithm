#coding: utf-8

"""
在一个排序的链表中，存在重复的结点，
请删除该链表中重复的结点，重复的结点不保留，
返回链表头指针。 例如，链表1->2->3->3->4->4->5
处理后为 1->2->5

"""

class ListNode(object):
    def __init__(self, x, node=None):
        self.val = x
        self.next = node


class Solution(object):
    def deleteDucurrentlication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead

        first = ListNode(-1)
        first.next = pHead
        current = pHead
        prev = first
        while current and current.next:
            if current.val == current.next.val:
                val = current.val
                while current and current.val == val:
                    current = current.next
                prev.next = current
            else:
                prev = current
                current = current.next
        return first.next


n = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
s = Solution()
s.deleteDucurrentlication(n)


"""
递归版, 有时间理解一下：

class Solution {
public:
    ListNode* deleteDuplication(ListNode* pHead)
    {
        if (pHead==NULL)
            return NULL;
        if (pHead!=NULL && pHead->next==NULL)
            return pHead;
                 
        ListNode* current;
         
        if ( pHead->next->val==pHead->val){
            current=pHead->next->next;
            while (current != NULL && current->val==pHead->val)
                current=current->next;
            return deleteDuplication(current);                     
        }
         
        else {
            current=pHead->next;
            pHead->next=deleteDuplication(current);
            return pHead;
        }    
    }
};
"""