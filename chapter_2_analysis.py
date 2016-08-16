__author__ = 'kfranko'

# notes for Chapter 2 - Analysis

'''
Self Check
Write two Python functions to find the minimum number in a list.
The first function should compare each number to every other number on the list.
O(n2)O(n2). The second function should be linear O(n)O(n).
'''
import time
from random import randrange


def func1(n):
    # O(n^2) (quadratic)
    # compare every number to every other number
    min_number = n[0]
    for i in n:
        for j in n:
            curr_min = min(i,j)
            min_number = min(curr_min,min_number)
    return min_number

list_of_nums = [6,4,3,8,7,9,8,7]

func1(list_of_nums)

def func2(n):
    # linear function O(n)
    min_number = n[0]
    # need to keep lowest number updated, and only loop through once
    for i in n:
        min_number = min(i,min_number)
    return min_number


func2(list_of_nums)

# test timing:

for listsize in range(1000, 10001, 1000):
    alist = [randrange(100000) for x in range(listsize)]
    start = time.time()
    print(func2(alist))
    end = time.time()
    print("size: %d time: %f" % (listsize, end-start))