'''
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        # 数组排序（从小到大）
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                return result
            # 剪枝
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 双指针
            left = i + 1
            right = len(nums) - 1
            while right > left:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ > 0:
                    right -= 1
                elif sum_ < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # 跳过相同的元素以避免重复
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1

                    right -= 1
                    left += 1

        return result

if __name__ == "__main__":
    nums =[-1, 0, 1, 2, -1, -4]
    solve=Solution()
    print(solve.threeSum(nums))