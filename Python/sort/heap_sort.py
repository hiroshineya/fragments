#!/usr/bin/python
# -*- coding: utf-8 -*-
# Heap sort

heap = []
num = 0

def push_heap(v):
    global heap
    global num
    # 最後尾に追加。
    heap[num] = v
    num += 1
    i = num
    j = i / 2
    # 追加した値を親と比較。親が大きければ、入替え。
    # ルートノードは最小値となる。
    while i>1 and heap[i-1]<heap[j-1]:
        t = heap[i-1]
        heap[i-1] = heap[j-1]
        heap[j-1] = t
        i = j
        j = i/2

def pop_min():
    global heap
    global num
    # ルートの値を取得(push処理にて最小値)
    r = heap[0]
    num -= 1
    # 要素が少なくなったので、単純に最後尾値をルートに持ってくる
    heap[0] = heap[num]
    i = 1
    j = i * 2
    # ルート値が最小となるようソート
    while j <= num:
        # 子のノードを比較して、小さい値のノードと比較する
        if j+1<=num and heap[j-1]>heap[j]:
            j += 1
        # 値入替え
        if heap[i-1]>heap[j-1]:
            t = heap[i-1]
            heap[i-1] = heap[j-1]
            heap[j-1] = t
        i = j
        j = i * 2
    return r

def sort(vals):
    global heap
    global num
    heap = vals[:]
    for i in range(len(heap)):
        heap[i] = None
    num = 0
    
    # push all values
    for i in range(len(vals)):
        push_heap(vals[i])
    
    # pop all values
    i = 0
    while num > 0:
        vals[i] = pop_min()
        i += 1
    
    return vals

if __name__ == "__main__":
    test_vals = [8, 3, 9, 2, 4, 6, 0, 1, 7, 5]
    print 'origin'
    print test_vals
    print ''
    test_vals = sort(test_vals)
    print ''
    print 'result'
    print test_vals
