#!/usr/bin/python


def bubble_sort(a):
    n = len(a)
    if n <= 1:
        return a
    for i in range(n):
        flag = False
        j = 0
        while j < (n - i - 1):
            if a[j] > a[j+1]:
                a[j] ^= a[j+1] # swap
                a[j+1] ^= a[j]
                a[j] ^= a[j+1]
                flag = True
            j += 1
        if not flag:
            break
    return a


def insert_sort(a):
    n = len(a)
    if n <= 1:
        return a
    for i in range(n)[1:]:
        value = a[i]
        j = i - 1
        while j >= 0:
            if a[j] > value:
                a[j+1] = a[j]
            else:
                break
            j -= 1
        a[j+1] = value
    return a


def select_sort(a):
    n = len(a)
    if n <= 1:
        return a
    for i in range(n):
        min_val = a[i]
        j = i + 1
        while j < n:
            if a[j] < min_val:
                min_val ^= a[j]
                a[j] ^= min_val
                min_val ^= a[j]
            j += 1
    return a


def partation(a, p, r):
    val = a[r]
    i = p
    j = p
    while j < r-1:
        if a[j] < val:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            i += 1
        j += 1
    if a[i] > val:
        temp = a[i]
        a[i] = a[r]
        a[r] = temp
    return i


def quick_sort(a, p, r):
    if p >= r:
        return a
    q = partation(a, p, r)
    quick_sort(a, p, q-1)
    quick_sort(a, q+1, r)
    return a


def merge(a, b):
    ret = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            ret.append(a[i])
            i += 1
        else:
            ret.append(b[j])
            j += 1
    if j < len(b):
        ret.extend(b[j:])
    if i < len(a):
        ret.extend(a[i:])
    return ret


def merge_sort(s):
    n = len(s)
    if n <= 1:
        return s
    mid = n/2
    a = merge_sort(s[:mid])
    b = merge_sort(s[mid:])
    return merge(a, b)


if __name__ == "__main__":
    data = [3, 6, 1, 4, 5, 2, 8, 7, 3]
    print bubble_sort(data)
    print insert_sort(data)
    print select_sort(data)
    print quick_sort(data, 0, len(data)-1)
    print merge_sort(data)
