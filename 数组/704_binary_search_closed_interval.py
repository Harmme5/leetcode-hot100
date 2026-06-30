from typing import List
'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果 target 存在返回下标，否则返回 -1。

你必须编写一个具有 O(log n) 时间复杂度的算法。
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            middle = left + (right-left)//2
            if nums[middle]<target:
                left = middle +1
            elif nums[middle]>target:
                right = middle
            else:
                return middle
        return -1

if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    solve = Solution()
    print(solve.search(nums,target))