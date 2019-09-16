# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

def forever_loop():
    i = 0
    nums = [1,2,3]
    while i <= len(nums):
        nums[i] = 0
        print('hello %d' % i)
        i += 1
    return

if __name__ == '__main__':
    forever_loop()
