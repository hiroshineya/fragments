#!/usr/bin/python
# -*- coding: utf-8 -*-
# Bubble sort

def sort(vals):
    cnt = 0
    for i in range(len(vals)):
        for j in range(len(vals)-1, i, -1):
            cnt += 1
            print vals[j]
            print vals
            if vals[j] < vals[j-1]:
                t = vals[j]
                vals[j] = vals[j-1]
                vals[j-1] = t
        print '--'
    print "cnt:%d" % cnt
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
