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
    # took up to 53 secs. to get through 10000


func2(list_of_nums)

# test timing:

for listsize in range(1000, 10001, 1000):
    alist = [randrange(100000) for x in range(listsize)]
    start = time.time()
    print(func2(alist))
    end = time.time()
    print("size: %d time: %f" % (listsize, end-start))


#### Lists:


# let's look at 4 different ways to generate a list of n numbers starting at 0:

# for loop and create list by concatenation:

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

# append instead of concatenation

def test2():
    l = []
    for i in range(1000):
        l.append(i)

# using list comprehension

def test3():
    l = [i for i in range(1000)]

# using the range function wrapped by a call to the list constructor:

def test4():
    l = list(range(1000))



# use timeit module to measure each function:

import Timer # must be a python 3 thing, don't have it

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")



# book's results:

# concat  6.54352807999 milliseconds
# append  0.306292057037 milliseconds
# comprehension  0.147661924362 milliseconds
# list range  0.0655000209808 milliseconds

# list comprehension is twice as fast as a for loop with append operation; why is this?









