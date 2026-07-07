from typing import Optional
'''
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建虚拟头部节点以简化删除过程
        dummy_head = ListNode(next=head)

        # 遍历列表并删除值为val的节点
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy_head.next

# 数组转链表工具
def arr_to_link(arr):
    if not arr:
        return None
    dummy = ListNode()
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

# 链表转数组打印工具
def link_to_arr(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

if __name__ == "__main__":
    solve = Solution()
    arr = [7, 7, 7, 7]
    val = 7
    # 数组转为链表头节点
    head = arr_to_link(arr)
    # 传入两个参数
    new_head = solve.removeElements(head, val)
    # 转数组输出结果
    print(link_to_arr(new_head))  # 输出 []