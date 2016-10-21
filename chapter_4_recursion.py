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

def ispalindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return ispalindrome(word[1:-1])



# starter code from book:

from test import testEqual
def removeWhite(s):
    s = ''.join(e for e in s if e.isalnum())
    return s

string2 = "madam i’m adam!!!!"

strip_string = ''.join(e for e in s if e.isalnum())

removeWhite(string)

from test import testEqual
def removeWhite(s):
    s = ''.join(e for e in s if e.isalnum())
    return s

def isPal(s):
    if len(s) < 2: return True
    if s[0] != s[-1]: return False
    return isPal(s[1:-1])

testEqual(isPal(removeWhite("x")),True)
testEqual(isPal(removeWhite("radar")),True)
testEqual(isPal(removeWhite("hello")),False)
testEqual(isPal(removeWhite("")),True)
testEqual(isPal(removeWhite("hannah")),True)
testEqual(isPal(removeWhite("madam i'm adam")),True)



## visualizing recursion:


# drawing a recursive spiral:

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()


# drawing a recursive tree:

import turtle

from random import randint

randint(15,45)


def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()


'''Self Check
Modify the recursive tree program using one or all of the following ideas:

Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.

Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.

Modify the angle used in turning the turtle so that at each branch point the angle is selected at random
in some range. For example choose the angle between 15 and 45 degrees. Play around to see what looks good.
    - use a stack? store each random angle, then pop them off to go backward? for some reason can't install
    any packages in pycharm at the moment...

Modify the branchLen recursively so that instead of always subtracting the same amount you subtract a
random amount in some range.'''

from pythonds.basic.stack import Stack

rStack = Stack()