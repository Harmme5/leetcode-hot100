from typing import List
'''
给你一个由 `n` 个整数组成的数组 `nums` ，和一个目标值 `target` 。
请你找出并返回满足下述全部条件且**不重复**的四元组 `[nums[a], nums[b], nums[c], nums[d]]` （若两个四元组元素一一对应，则认为两个四元组重复）：

- `0 <= a, b, c, d < n`
- `a`、`b`、`c` 和 `d` **互不相同**
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

你可以按 任意顺序 返回答案 。
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        for k in range(n):
            if nums[k] > target and nums[k] > 0 and target > 0:  # 剪枝（可省）
                break
            # sum_不可能等于target的情况
            if nums[k] > target and nums[k] > 0:
                continue
            # 跳过相同的元素以避免重复
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            for i in range(k + 1, n):
                if nums[k] + nums[i] > target and target > 0:  # 剪枝（可省）
                    break
                # 跳过相同的元素以避免重复
                if i > k + 1 and nums[i] == nums[i - 1]:  # i>0防止数组越界
                    continue
                left = i + 1
                right = n - 1
                while right > left:
                    sum_ = nums[k] + nums[i] + nums[left] + nums[right]
                    if sum_ < target:
                        left += 1
                    elif sum_ > target:
                        right -= 1
                    else:
                        result.append([nums[k], nums[i], nums[left], nums[right]])
                        # 跳过相同的元素以避免重复
                        while right > left and nums[right] == nums[right - 1]:
                            right -= 1
                        while right > left and nums[left] == nums[left + 1]:
                            left += 1

                        right -= 1
                        left += 1
        return result
if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target=0
    solve = Solution()
    print(solve.fourSum(nums,target))