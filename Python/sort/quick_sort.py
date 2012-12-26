#!/usr/bin/python
# -*- coding: utf-8 -*-
# Quick sort


def pivot(vals, i, j):
    k = i + 1
    while k<j and vals[i]==vals[k]:
        k += 1
    if k>j:
        return -1
    if vals[i]>=vals[k]:
        return i
    return k

def partition(vals, i, j, x):
    l = i
    r = j
    while l<=r:
        while l<=j and vals[l]<x:
            l += 1
        while r>=i and vals[r]>=x:
            r -= 1
        if l>r:
            break
        t = vals[l]
        vals[l] = vals[r]
        vals[r] = t
        l += 1
        r -= 1
    return l

def quick_sort(vals, i, j):
    if i==j:
        return
    p = pivot(vals, i, j)
    if p!=-1:
        k = partition(vals, i, j, vals[p])
        quick_sort(vals, i, k-1)
        quick_sort(vals, k, j)

def sort(vals):
    quick_sort(vals, 0, len(vals)-1)
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
