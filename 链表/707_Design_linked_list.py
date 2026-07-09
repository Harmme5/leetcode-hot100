class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.dummy_head.next
        for i in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1

    # 辅助打印函数
    def print_list(self):
        res = []
        cur = self.dummy_head.next
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        print("链表：[" + ",".join(res) + f"], size={self.size}")


# ====================== 测试用例 ======================
def test_linked_list():
    print("===== 测试1：空链表查询、非法索引 =====")
    obj = MyLinkedList()
    print("get(0):", obj.get(0))   # 空链表，返回-1
    print("get(-1):", obj.get(-1)) # 负数索引
    print("get(99):", obj.get(99))# 超范围
    obj.print_list()

    print("\n===== 测试2：头插元素 =====")
    obj.addAtHead(1)
    obj.addAtHead(2)
    obj.addAtHead(3)
    obj.print_list()  # [3,2,1]
    print("get(0):", obj.get(0)) # 3
    print("get(2):", obj.get(2)) # 1

    print("\n===== 测试3：尾插元素 =====")
    obj.addAtTail(10)
    obj.addAtTail(20)
    obj.print_list() # [3,2,1,10,20]

    print("\n===== 测试4：指定位置插入 =====")
    obj.addAtIndex(0, 99)  # 头部插入
    obj.addAtIndex(3, 55)  # 中间插入
    obj.addAtIndex(obj.size, 88) # 尾部插入
    obj.addAtIndex(99, 77) # 非法索引，不生效
    obj.print_list() # [99,3,2,55,1,10,20,88]

    print("\n===== 测试5：删除指定位置 =====")
    obj.deleteAtIndex(0)   # 删头
    obj.deleteAtIndex(3)   # 删中间
    obj.deleteAtIndex(obj.size - 1) # 删尾
    obj.deleteAtIndex(99)  # 非法索引，不生效
    obj.print_list()

    print("\n===== 测试6：清空链表场景 =====")
    while obj.size > 0:
        obj.deleteAtIndex(0)
    obj.print_list()
    print("空链表get(0):", obj.get(0))

    print("\n===== 测试7：LeetCode官方样例流程 =====")
    ll = MyLinkedList()
    ll.addAtHead(1)
    ll.addAtTail(3)
    ll.addAtIndex(1, 2) # [1,2,3]
    print("get(1):", ll.get(1)) # 2
    ll.deleteAtIndex(1) # [1,3]
    print("get(1):", ll.get(1)) # 3
    ll.print_list()


# 执行测试
if __name__ == "__main__":
    test_linked_list()