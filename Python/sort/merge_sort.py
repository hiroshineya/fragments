#!/usr/bin/python
# -*- coding: utf-8 -*-
# Merge sort

# マージ処理
def merge(valsA, valsB, vals):
    print '-- merge'
    print valsA
    print valsB
    print vals
    i = 0
    j = 0
    while i<len(valsA) or j<len(valsB):
        if j>=len(valsB) or (i<len(valsA) and valsA[i]<valsB[j]):
            vals[i+j] = valsA[i]
            i += 1
        else:
            vals[i+j] = valsB[j]
            j += 1
    print '-'
    print vals

# 再帰ソート実処理
def merge_sort(vals):
    print '-- merge_sort'
    print vals
    if len(vals) > 1:
        m = len(vals) / 2
        n = len(vals) - m
        valsA = vals[0:m]
        valsB = vals[m:len(vals)]
        merge_sort(valsA)
        merge_sort(valsB)
        merge(valsA, valsB, vals)

# ソートIF関数
def sort(vals):
    merge_sort(vals)
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
