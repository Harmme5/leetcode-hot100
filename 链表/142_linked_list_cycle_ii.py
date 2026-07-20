# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
给定一个链表的头节点 head ，返回链表开始入环的第一个节点。如果链表无环，则返回 null。
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。不允许修改链表。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点

示例 3：
输入：head = [1], pos = -1
输出：返回 null
'''
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If there is a cycle, the slow and fast pointers will eventually meet
            if slow == fast:
                # Move one of the pointers back to the start of the list
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        # If there is no cycle, return None
        return None


if __name__ == "__main__":
    # 测试用例1：带环链表
    head1 = ListNode(3)
    node2 = ListNode(2)
    node0 = ListNode(0)
    node4 = ListNode(-4)
    head1.next = node2
    node2.next = node0
    node0.next = node4
    node4.next = node2  # 环指向第二个节点

    sol = Solution()
    res1 = sol.detectCycle(head1)
    print(f"测试用例1环入口节点值: {res1.val if res1 else '无环'}")

    # 测试用例2：无环链表
    head2 = ListNode(1)
    head2.next = ListNode(2)
    res2 = sol.detectCycle(head2)
    print(f"测试用例2环入口节点值: {res2.val if res2 else '无环'}")