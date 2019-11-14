from bf import bf
from kmp import kmp_search
import time


def single_match_test():
    tests = [
        ("ABCDABD", "BBCABCDABABCDABCDABDEABCDABD"),  # [13,21]
        ("aa", "aaaaaaaa"),  # [0,1,2,4,5,6]
        ("AAACAAAA", "AAACAAADAAACAAAsAAACAAAAAAACAAAA")  # [16,24]
    ]
    for (p, s) in tests:
        print(p, s)
        start = time.time()
        print(bf(s, p))
        print((time.time() - start) * 1000.)


if __name__ == '__main__':
    single_match_test()
