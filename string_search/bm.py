"""
bm算法：效率高于kmp算法，且易于理解，各种文本编辑器的"查找"功能（Ctrl+F），大多采用Boyer-Moore算法。
两张移动表：坏字符表和好前缀表
时间复杂度：最好情况下的时间复杂度为O(n/m)，最坏情况下时间复杂度为O(m·n)。

"""


def build_bad_charcter_table(pattern):
    bad_ct = {}
    for i, char in enumerate(pattern):
        bad_ct[char] = i  # 记录坏字符最靠右的位置，之所以是最靠右，因为bm算法是从右到左匹配的，所以不能漏掉右边（先比较）的字符
    return bad_ct


def build_good_postfix_table(pattern):
    good_pt = {"": 0}
    m = len(pattern)
    last = m - 1
    for i in range(m):
        gs = pattern[(last - i):]  # 好后缀u，长度为i
        """
        如果pattern前面还有与u相同的字符u`(最靠右)，则位置是u的最后一位减u`的最后一位，如果没有，则需要找u的后缀
        """
        for j in range(last - i):
            bgs = pattern[j:j + i + 1]  # 长度为i
            if gs == bgs:
                # print(gs, bgs, i, j, m - j - i)
                good_pt[gs] = last - j - i  # u的最后一位减u`的最后一位,移动位数
    return good_pt


def bm_search(s, pattern):
    m = len(pattern)
    n = len(s)
    bad_ct = build_bad_charcter_table(pattern)
    good_pt = build_good_postfix_table(pattern)

    result = []
    i, j = 0, m
    while i < n:
        while j > 0:
            if i + j - 1 >= n:  # 当无法继续向下搜索就返回值
                return result
            a = pattern[j - 1:]  # pattern中的匹配内容
            b = s[i + j - 1:i + m]  # string中的匹配内容
            if a == b:
                j = j - 1
            else:
                i = i + max(good_pt.setdefault(a[1:], m),
                            j - bad_ct.setdefault(s[i + j], -1))  # 坏字符不在pattern中，默认设置为-1，坏字符移动位数可能是负值
                j = m
        if j == 0:
            result.append(i)
            i += 1
            j = m
    return result


def single_match_test():
    tests = [
        ("ABCDABD", "BBCABCDABABCDABCDABDEABCDABD"),
        ("aa", "aaaaaaaa"),
        ("abcab", "abcabcabcab"),
        ("AAACAAAA", "AAACAAADAAACAAAsAAACAAAAAAACAAAA")
    ]
    for (p, s) in tests:
        print(p, s)
        print("good postfix:", build_good_postfix_table(p))
        print("bad character: ", build_bad_charcter_table(p))
        print(bm_search(s, p))


if __name__ == '__main__':
    single_match_test()
