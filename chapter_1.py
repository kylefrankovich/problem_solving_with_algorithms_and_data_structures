__author__ = 'kfranko'

# notes for Chapter 1

## Control Structures
'''Self Check
Test your understanding of what we have covered so far by trying the following exercise.
Modify the code from Activecode 8 so that the final list only contains a single copy of each letter.'''

wordlist = ['cat', 'dog', 'rabbit']
letterlist = []
for aword in wordlist:
    for aletter in aword:
        if aletter not in letterlist:
            letterlist.append(aletter)
print(letterlist)

# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

# List Comprehension:

# using a for loop:
sqlist = []
for x in range(1, 11):
    sqlist.append(x * x)

sqlist

# using list comprehension:
sqlist = [x * x for x in range(1, 11)]

sqlist

sqlist = [x * x for x in range(1, 11) if x % 2 != 0]

sqlist

[ch.upper() for ch in 'comprehension' if ch not in 'aeiou']

'''Self Check
Test your understanding of list comprehensions by redoing Activecode 8 using list comprehensions.
For an extra challence, see if you can figure out how to remove the duplicates.'''

# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']

wordlist = ['cat', 'dog', 'rabbit']
letterlist = []
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)

letterlist = [aletter for word in wordlist for aletter in word]

letterlist

## Exception Handling
import math

anumber = -23
try:
    print(math.sqrt(anumber))
except:
    print("Bad Value for square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(anumber)))

if anumber < 0:
    raise RuntimeError("You can't use a negative number")
else:
    print(math.sqrt(anumber))



## Defining Functions

'''Self Check
Here’s a self check that really covers everything so far. You may have heard of the infinite monkey theorem?
The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will
almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey
with a Python function. How long do you think it would take for a Python function to generate just one sentence
of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”

You’re not going to want to run this one in the browser, so fire up your favorite Python IDE.
The way we’ll simulate this is to write a function that generates a string that is 27 characters long by
choosing random letters from the 26 letters in the alphabet plus the space. We’ll write another function that
will score each generated string by comparing the randomly generated string to the goal.

A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done.
If the letters are not correct then we will generate a whole new string.To make it easier to follow your
program’s progress this third function should print out the best string generated so far and its score every 1000 tries.'''


target = "methinks it is like a weasel"
len(target)

import random, string

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

blah = randomword(8)
len(blah)
first_word = 'methinks'
len(first_word)


alphabet = list(string.ascii_lowercase)
alphabet.append(' ')


# generate a random set of words as long as the target:
def generate(n):
    return ''.join(random.choice(alphabet) for i in range(n))

blah = generate(len(target))
blah
len(blah)

import numpy

correct = [0,1,1]
numpy.mean(correct)

def score(input):
    score_results = []
    for i in range(1,len(input)):
        if input[i] == target[i]:
            score_results.append(1)
        else:
            score_results.append(0)
    #return numpy.mean(score_results)
    return score_results

blah_results = score(blah)

numpy.mean(blah)

close_target = "methinks it is like a weaszz"
target

close_results = score(close_target)

actual_results = "methinks it is like a weasel"

score(actual_results)

target = 'abc'

def infinite_monkey(target):
    accuracy = [0]
    best_string_generated = []
    while accuracy < 1:
        cur_string = generate(len(target))
        cur_acc = score(cur_string)
        accuracy = max(accuracy, cur_acc)


cur_string = generate(len(target))
cur_string