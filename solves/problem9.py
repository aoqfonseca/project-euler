# -*- coding: utf-8 -*-

sum = 1000
range_a = range(1, sum/3)
for i in range_a:
    for j in range(i+1, sum/2):
        c = sum - i - j
        if (i**2+j**2 == c**2):
            print i,j,c
            print i*j*c

