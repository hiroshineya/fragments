#!/usr/bin/python
# -*- coding: utf-8 -*-
# Selection sort

def sort(vals):
    cnt = 0
    for i in range(len(vals)):
        print "- %d" % i
        min_v = vals[i]
        for j in range(i, len(vals)):
            cnt += 1
            print j
            if min_v > vals[j]:
                t = vals[j]
                vals[j] = min_v
                min_v = t
        vals[i] = min_v
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
