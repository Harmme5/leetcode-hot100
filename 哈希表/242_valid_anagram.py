"""
LeetCode 242. 有效的字母异位词
给定两个字符串 `s` 和 `t` ，编写一个函数来判断 `t` 是否是 `s` 的 字母异位词。
字母异位词是通过重新排列不同单词或短语的字母而形成的单词或短语，并使用所有原字母一次。
"""
#数组作为哈希表
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            record[ord(i)-ord("a")]+=1
        for i in t:
            record[ord(i)-ord("a")]-=1
        for i in range(26):
            if record[i]!=0:
                return False
        return True

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    solve=Solution()
    print(solve.isAnagram(s,t))