#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# @Time : 19-11-7 下午3:47 
# @Author : shixi 
# @Site : shixi.zhang@cloudminds.com 
# @File : ac_automation.py 
# AC自动机算法
import ahocorasick


class AHReplace:
    """
    使用公开的ac库，pyahocorasick进行ac匹配
    """

    def __init__(self, replace_dict):
        new_replace_dcit = replace_dict.copy()
        for word in replace_dict.values():
            new_replace_dcit[word] = word
        del replace_dict
        self.replace_dict = new_replace_dcit

        A = ahocorasick.Automaton()
        for word in self.replace_dict.keys():
            A.add_word(word, word)
        A.make_automaton()
        self.A = A

    def replace_words(self, text):
        words = [a_i[1] for a_i in list(self.A.iter(text))]
        words = sorted(words, key=lambda item: len(item), reverse=True)
        replace_words = []
        """
        长字符优先替换，先替换为某个特定字符，避免出现重复替换的问题
        """
        for w in words:
            replace_words.append(self.replace_dict[w])
            text = text.replace(w, "**{:d}**".format(len(replace_words) - 1))
        for i, r_w in enumerate(replace_words):
            text = text.replace("**{:d}**".format(i), r_w)
        return text

