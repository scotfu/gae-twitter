#! /usr/bin/env python
#coding=utf-8
import random
 
 
def exchange(i, j):
    return j, i
 
 
def random_partition(a, start, end):
    i=random.randint(start, end)
    i, end = end, i
    partition(a, start, end)
 
 
def partition(a, start, end):
    x=a[end]
    i=start-1
    for j in range(start, end):
        if a[j]<=x:
            i+=1
            a[i], a[j]=exchange(a[i], a[j])
    a[i+1], a[end]= exchange(a[i+1], a[end])
    return i+1
 
 
def qsort(a, start, end):
    if start<end:
        middle=partition(a, start, end)
        qsort(a, start, middle-1)
        qsort(a, middle+1, end)
    return a
