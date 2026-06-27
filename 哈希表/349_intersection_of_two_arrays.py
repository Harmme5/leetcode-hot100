from typing import List

"""
给定两个数组，编写一个函数来计算它们的交集。
"""
#使用字典和集合写法
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
		#定义字典，作为哈希表，存储一个数组的所有元素
        table={}
		#将nums1数组中的元素存到哈希表中，key为数组的元素，value为出现的次数
        for num in nums1:
            table[num]=table.get(num,0)+1
		#定义集合，用于存储结果
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]

        return list(res)
#使用数组
class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = [0]*1001
        count2 = [0]*1001
        result = []
        for i in range(len(nums1)):
            count1[nums1[i]]+=1
        for j in range(len(nums2)):
            count2[nums2[j]]+=1
        for k in range(1001):
            if count1[k]*count2[k]>0:
                result.append(k)
        return result

if __name__ == "__main__":
    solve = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(solve.intersection(nums1,nums2))