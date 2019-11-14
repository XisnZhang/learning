"""
任务：字符串匹配，在一个文本或者较长的一段字符串中，找出一个指定字符串（Pattern），并返回其位置

算法：bf(Brute-Force),暴力搜索
时间复杂度为：o(m*n)

"""


def bf(s, pattern):
    result = []
    m = len(pattern)
    n = len(s)
    if m > n:
        return -1
    i, j = 0, 0
    for i in range(n - m + 1):
        for j in range(m):
            if s[i] == pattern[j]:
                i += 1
                j += 1
            else:
                i = i - (j - 1)
                j = 0
                break
        if j == m:
            result.append(i - j)
    return result
