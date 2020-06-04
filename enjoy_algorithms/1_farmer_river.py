#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
问题描述：
一个农夫在河边要过河，但是他带着一匹狼、一只羊和一颗白菜。他需要用船将这三样东西运至对岸，然而，这艘船的空间有限，只容得下他自己和另一样东西
（或狼或羊或白菜）。若他不在场看管的话，狼就会吃羊，羊就会去吃白菜。此人如何才能过河。
"""


class solution:
    def __init__(self):
        self.state = [1] * 3  # #[wolf,sheep, cabbage]
        self.candidate_state = [
            [-1, 0, 0],
            [0, -1, 1],
            [0, 0, -1],
            [0, 0, 0],
            [1, 0, 0],
            [0, 0, 1],
            [0, 1, 0]
        ]

    def farmer_river(self):
        state = self.state
        length = len(state)
        while sum(state) != 0:
            for s in self.candidate_state:
                new_state = [s[i] + state[i] for i in range(length)]
                if -1 in new_state or 2 in new_state:
                    continue
                state = new_state
                print(state)


if __name__ == '__main__':
    solution().farmer_river()
