from typing import Optional
'''
题意：反转一个单链表。

示例: 输入: `1->2->3->4->5->NULL`

	  输出: `5->4->3->2->1->NULL`
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre # 反转指针

            pre = cur
            cur = temp
        return pre

# 辅助函数：数组转链表
def list_to_link(arr: list) -> Optional[ListNode]:
    if not arr:
        return None
    dummy = ListNode()
    p = dummy
    for num in arr:
        p.next = ListNode(num)
        p = p.next
    return dummy.next

# 辅助函数：链表转数组，方便打印对比结果
def link_to_list(head: Optional[ListNode]) -> list:
    res = []
    p = head
    while p:
        res.append(p.val)
        p = p.next
    return res

if __name__ == "__main__":
    sol = Solution()

    # 测试用例1：普通多节点链表
    arr1 = [1,2,3,4,5]
    head1 = list_to_link(arr1)
    rev1 = sol.reverseList(head1)
    print(f"原数组 {arr1} 反转后：{link_to_list(rev1)}")

    # 测试用例2：两个节点
    arr2 = [1,2]
    head2 = list_to_link(arr2)
    rev2 = sol.reverseList(head2)
    print(f"原数组 {arr2} 反转后：{link_to_list(rev2)}")

    # 测试用例3：单个节点
    arr3 = [8]
    head3 = list_to_link(arr3)
    rev3 = sol.reverseList(head3)
    print(f"原数组 {arr3} 反转后：{link_to_list(rev3)}")

    # 测试用例4：空链表
    arr4 = []
    head4 = list_to_link(arr4)
    rev4 = sol.reverseList(head4)
    print(f"原数组 {arr4} 反转后：{link_to_list(rev4)}")