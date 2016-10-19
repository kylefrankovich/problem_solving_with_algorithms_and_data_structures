# notes for Chapter 3 - Basic Data Structures

'''We will begin our investigation with a simple problem that you already
know how to solve without using recursion. Suppose that you want to calculate
the sum of a list of numbers such as: [1,3,5,7,9]
. An iterative function that computes the sum is shown in ActiveCode 1.
The function uses an accumulator variable (theSum) to compute a running total
of all the numbers in the list by starting with 0
 and adding each number in the list.'''

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum([1,3,5,7,9]))


# solve same problem recursively:

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:]) # here the function calls itself,
   # and is the reason why this algorithm is recursive

print(listsum([1,3,5,7,9]))

blah = [1,3,5,7,9]

blah[1:]



# using recursion to convert an integer to a string in any base:

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16))

print(toStr(14,16))


# self check:

'''Write a function that takes a string as a parameter and
returns a new string that is the reverse of the old string.'''

from test import testEqual
def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

testEqual(reverse("hello"),"olleh")
testEqual(reverse("l"),"l")
testEqual(reverse("follow"),"wollof")
testEqual(reverse(""),"")

reverse_string = reverse("hello")

'''Write a function that takes a string as a parameter and returns
True if the string is a palindrome, False otherwise. Remember that
a string is a palindrome if it is spelled the same both forward and
backward. For example: radar is a palindrome. for bonus points
palindromes can also be phrases, but you need to remove the spaces
and punctuation before checking. for example: madam i’m adam is a
palindrome. Other fun palindromes include:'''


def palindromecheck(s):
    strip_string = ''.join(e for e in s if e.isalnum())
    is_palindrome = True
    while is_palindrome:
        


s = "madam i’m adam!!!!"

strip_string = ''.join(e for e in s if e.isalnum())