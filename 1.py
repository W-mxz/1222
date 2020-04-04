#!usr/bin/python
# -*- coding:utf-8 -*-
import itertools
S = 0
n = ''
N = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (j != k) and (i != k):
                n = str(i) + str(j) + str(k)
                N.append(n)
                S = S + 1

print(N)
