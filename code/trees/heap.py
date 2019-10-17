#!/usr/bin/python
# 堆的插入（自底向上）
# 堆化（自顶向下）
# 建堆

class BigHeap(object):
    def __init__(self):
        self.heap = list()
        self.heap.append(None) # heap 从下标1开始

    def swap(self, a, b):
        self.heap[a] ^= self.heap[b]
        self.heap[b] ^= self.heap[a]
        self.heap[a] ^= self.heap[b]

    def insert_heap(self, val):
        self.heap.append(val)
        i = len(self.heap)-1
        while i/2 > 0 and self.heap[i] > self.heap[i/2]:
            self.swap(i, i/2)
            i = i/2

    def heapify(self, i):
        while True:
            max_position = i
            if i*2 < len(self.heap) and self.heap[i] < self.heap[i*2]:
                max_position = i*2
            if i*2+1 < len(self.heap) and self.heap[i] < self.heap[i*2+1] and self.heap[max_position] < self.heap[2*i+1]: # 堆里有相同的数字
                max_position = i*2+1
            if max_position == i:
                break
            self.swap(i, max_position)
            i = max_position

    def delete_heap(self, val):
        if val not in self.heap:
            return
        pos = self.heap.index(val)
        self.heap[pos] = self.heap[-1]
        self.heap.remove(val)
        self.heapify(pos)


    def build_heap(self):
        i = len(self.heap)/2
        while i > 0:
            self.heapify(i)
            i -= 1

class SmallHeap(object):
    def __init__(self):
        self.heap = list()
        self.heap.append(None) # heap 从下标1开始

    def swap(self, a, b):
        self.heap[a] ^= self.heap[b]
        self.heap[b] ^= self.heap[a]
        self.heap[a] ^= self.heap[b]

    def insert_heap(self, val):
        self.heap.append(val)
        i = len(self.heap)-1
        while i/2 > 0 and self.heap[i] < self.heap[i/2]:
            self.swap(i, i/2)
            i = i/2

    def heapify(self, i):
        while True:
            min_pos = i
            if i*2 < len(self.heap) and self.heap[i] > self.heap[i*2]:
                min_pos = i*2
            if i*2+1 < len(self.heap) and self.heap[i] > self.heap[i*2+1] and self.heap[min_pos] > self.heap[i*2+1]:# 堆里有相同的数字
                min_pos = i*2+1
            if min_pos == i:
                break
            self.swap(i, min_pos)
            i = min_pos

    def delete_heap(self, val):
        if val not in self.heap:
            return
        pos = self.heap.index(val)
        self.heap[pos] = self.heap[-1]
        self.heap.remove(val)
        self.heapify(pos)

    def build_heap(self):
        i = len(self.heap)/2
        while i > 0:
            self.heapify(i)
            i -=1
