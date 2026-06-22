from typing import List
"""
LeetCode 1. 两数之和
题目：给定整数数组 nums 和整数目标值 target，返回两个相加等于 target 的下标
约束：
1. 每个输入恰好一组解
2. 同一个元素不能使用两次
3. 下标顺序不限
"""
#哈希表解法
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        records={}
        for index,value in enumerate(nums):
            if target-value in records:
                return [records[target-value],index]
            records[value]=index
        return []
        

# 暴力解法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]

if __name__ == '__main__':
    Solve=Solution1()
    nums=[2,7,6,3]
    target=9
    print(Solve.twoSum(nums,target))
