'''
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
'''
# 链表节点定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next=head)
        current = dummy_head

        # 必须有cur的下一个和下下个才能交换，否则说明已经交换结束了
        while current.next and current.next.next:
            temp = current.next  # 保存第一个待交换节点
            temp1 = current.next.next.next  # 保存下一组的开头

            # 交换两个节点
            current.next = current.next.next
            current.next.next = temp
            temp.next = temp1
            # current 跳到下一组的前驱
            current = current.next.next
        return dummy_head.next


# 辅助函数：数组转链表
def arr_to_link(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for num in arr[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return head


# 辅助函数：链表转数组打印
def link_to_arr(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


# 测试用例
if __name__ == "__main__":
    sol = Solution()

    # 测试1：偶数个节点 [1,2,3,4]
    arr1 = [1, 2, 3, 4]
    head1 = arr_to_link(arr1)
    new_head1 = sol.swapPairs(head1)
    print(f"输入 {arr1} 交换后：{link_to_arr(new_head1)}")

    # 测试2：奇数个节点 [1,2,3]
    arr2 = [1, 2, 3]
    head2 = arr_to_link(arr2)
    new_head2 = sol.swapPairs(head2)
    print(f"输入 {arr2} 交换后：{link_to_arr(new_head2)}")

    # 测试3：单个节点 [1]
    arr3 = [1]
    head3 = arr_to_link(arr3)
    new_head3 = sol.swapPairs(head3)
    print(f"输入 {arr3} 交换后：{link_to_arr(new_head3)}")

    # 测试4：空链表
    arr4 = []
    head4 = arr_to_link(arr4)
    new_head4 = sol.swapPairs(head4)
    print(f"输入 {arr4} 交换后：{link_to_arr(new_head4)}")