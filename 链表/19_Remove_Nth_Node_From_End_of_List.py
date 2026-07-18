'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 创建一个虚拟节点，并将其下一个指针设置为链表的头部
        dummy_head = ListNode(0, head)

        # 创建两个指针，慢指针和快指针，并将它们初始化为虚拟节点
        slow = fast = dummy_head

        # 快指针比慢指针快 n+1 步
        for i in range(n + 1):
            fast = fast.next

        # 移动两个指针，直到快速指针到达链表的末尾
        while fast:
            slow = slow.next
            fast = fast.next

        # 通过更新第 (n-1) 个节点的 next 指针删除第 n 个节点
        slow.next = slow.next.next

        return dummy_head.next

# 辅助函数：列表转链表
def list_to_linked(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for num in arr[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return head

# 辅助函数：链表转列表，方便打印结果
def linked_to_list(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

if __name__ == "__main__":
    '''
    测试说明：覆盖四种典型场景
    1. 删除链表中间节点
    2. 链表仅单个节点，删除唯一节点
    3. 删除原链表头节点
    4. 删除链表尾节点
    '''
    sol = Solution()

    # 测试用例1：常规 [1,2,3,4,5] 删除倒数第2个 → [1,2,3,5]
    arr1 = [1,2,3,4,5]
    n1 = 2
    head1 = list_to_linked(arr1)
    new_head1 = sol.removeNthFromEnd(head1, n1)
    print(f"测试用例1 输入:{arr1}, 删除倒数{n1}个 → 输出:{linked_to_list(new_head1)}")

    # 测试用例2：只有一个节点 [1] 删除倒数第1个 → []
    arr2 = [1]
    n2 = 1
    head2 = list_to_linked(arr2)
    new_head2 = sol.removeNthFromEnd(head2, n2)
    print(f"测试用例2 输入:{arr2}, 删除倒数{n2}个 → 输出:{linked_to_list(new_head2)}")

    # 测试用例3：删除头节点 [1,2] 删除倒数第2个 → [2]
    arr3 = [1,2]
    n3 = 2
    head3 = list_to_linked(arr3)
    new_head3 = sol.removeNthFromEnd(head3, n3)  # 修复：补上n3参数
    print(f"测试用例3 输入:{arr3}, 删除倒数{n3}个 → 输出:{linked_to_list(new_head3)}")

    # 测试用例4：删除尾节点 [1,2,3] 删除倒数第1个 → [1,2]
    arr4 = [1,2,3]
    n4 = 1
    head4 = list_to_linked(arr4)
    new_head4 = sol.removeNthFromEnd(head4, n4)
    print(f"测试用例4 输入:{arr4}, 删除倒数{n4}个 → 输出:{linked_to_list(new_head4)}")