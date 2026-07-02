from typing import List
'''
给你一个按 **非递减顺序** 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 **非递减顺序** 排序。

示例 1：

- 输入：nums \= [-4,-1,0,3,10]
- 输出：[0,1,9,16,100]
- 解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]

示例 2：

- 输入：nums \= [-7,-3,2,3,11]
- 输出：[4,9,9,49,121]
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        k = len(nums) -1
        result = [0] * len(nums)
        i = 0
        j = k
        while i<=j:
            if nums[i]*nums[i]>nums[j]*nums[j]:
                result[k] = nums[i]*nums[i]
                k-=1
                i+=1
            else:
                result[k] = nums[j]*nums[j]
                k-=1
                j-=1
        return result
if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    solve = Solution()
    print(solve.sortedSquares(nums))