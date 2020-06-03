import time

"""
时间复杂度为：o(m+n),并不是效率最高的匹配算法
"""


def kmp_prefix(pattern):
    m = len(pattern)
    prefix = [0] * (m + 1)  # 0位存-1，需要多一位
    prefix[0] = -1
    k = -1
    j = 0
    while j < m:
        if k == -1 or pattern[k] == pattern[j]:
            k += 1
            j += 1
            prefix[j] = k  # 相等的时候直接是前面的值+1
        else:
            k = prefix[k]  # 递归求解，不相等的时候需要回溯
    return prefix


def kmp_search(s, pattern):
    n = len(s)
    m = len(pattern)
    if n < m:
        return -1
    next_array = kmp_prefix(pattern)

    result = []
    i, j = 0, 0
    while i < n and j < m:
        if j == -1 or s[i] == pattern[j]:
            i += 1
            j += 1
        else:  # i的位置并未回溯，移动的是j的位置，
            j = next_array[j]
        if j == m:
            result.append(i - j)
            # #检索所有位置
            # #1、允许重叠
            j = next_array[j]
            # #2、不允许重叠
            # j = 0

    return result


if __name__ == '__main__':
    tests = [
        ("ABCDABD", "BBCABCDABABCDABCDABDEABCDABD"),
        ("aa", "aaaaaaaa"),
        ("abcab", "abcabcabcab"),
        ("AAACAAAA", "AAACAAADAAACAAAsAAACAAAAAAACAAAA")
    ]
    for (p, s) in tests:
        print(p, s)
        print(kmp_prefix(p))
        print(kmp_search(s, pattern=p))
        # print(compute_next_array(p))
        # print(get_next_table(p))
