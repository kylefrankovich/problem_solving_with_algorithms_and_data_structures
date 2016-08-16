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

def score(input,target):
    score_results = []
    for i in range(1,len(input)):
        if input[i] == target[i]:
            score_results.append(1)
        else:
            score_results.append(0)
    #return numpy.mean(score_results)
    return numpy.mean(score_results)

blah_results = score(blah)

numpy.mean(blah)

close_target = "methinks it is like a weaszz"
target

close_results = score(close_target)

actual_results = "methinks it is like a weasel"

score(actual_results)

target = 'abc'

def infinite_monkey(target):
    accuracy = 0
    count = 0
    best_string_generated = ''
    while accuracy < 1:
        cur_string = generate(len(target))
        cur_acc = score(cur_string,target)
        # accuracy = max(accuracy, cur_acc)
        if cur_acc > accuracy:
            best_string_generated = cur_string
            accuracy = cur_acc
        count += 1
        if count % 1000 == 0:
            print("current count: %d"%count)
            print("current best string so far: %s"%best_string_generated)
            print("current best score so far: %s"%accuracy)
    print count, best_string_generated, accuracy



target = 'abc'

infinite_monkey(target)

target_string = "methinks it is like a weasel"

infinite_monkey(target_string)

cur_string = generate(len(target_string))
cur_acc = score(cur_string,target_string)


# solution:

def generateOne(strlen):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    res = ''
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
    return res

# integer division issue here due to python 2.7, example he uses is with 3
def score(goal,teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame = numSame + 1
    return numSame / len(goal)

print(score('methinks it is like a weasel', generateOne(28)))

def main():
    goalstring = 'methinks it is like a weasel'
    newstring = generateOne(28)
    best = 0
    newscore = score(goalstring,newstring)
    while newscore < 1:
        if newscore > best:
            print(newscore, newstring)
            best = newscore
        newstring = generateOne(28)
        newscore = score(goalstring,newstring)

# additional goal suggested, adding modulo operator to print out best every million iterations



'''Self Check Challenge
See if you can improve upon the program in the self check by keeping letters that are correct
and only modifying one character in the best string so far. This is a type of algorithm in the
class of ‘hill climbing’ algorithms, that is we only keep the result if it is better than the previous one.'''


## Object Oriented Programming in Python

# fraction class example:

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum

     def __lt__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum < secondnum

     def __gt__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum > secondnum

     def __sub__(self, otherfraction):
         newnum = self.num*otherfraction.den - \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __mul__(self, otherfraction):
         newnum = self.num*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __truediv__(self, otherfraction):
         newnum = self.num * otherfraction.den
         newden = self.den * otherfraction.num

         common = gcd(nuenum,newden)

         return Fraction(newnum//common, newden/common)




x = Fraction(1,3)
y = Fraction(2,6)
print(x)
print(y)
print(x+y)
# error, need to write method above (works):
print(x-y)

print(x == y)
print('multiplication:')
# multiplication:
print(x*y)

#error; python version issue?
print('division:')
print(x/y)

# comparison operators:
print(x<y)
print(x>y)
print(x==y)

# Self Check
# To make sure you understand how operators are implemented in Python classes,
# and how to properly write methods, write some methods to implement *, /, and - .
# Also implement comparison operators > and <


# Inheritance: logic gates and circuits


class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
               raise RuntimeError("Error: NO EMPTY PINS")

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))

class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

# show AndGate class in action:

g1 = AndGate("G1")
g1.getOutput()

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0

# show OrGate class in action:

g2 = OrGate("G2")
g2.getOutput()

class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPin()

        if a==1:
            return 0
        else:
            return 1

# show NotGate class in action:

g3 = NotGate("G3")
g3.getOutput()


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

    #The call to setNextPin is very important for making connections (see Listing 13).
    # We need to add this method to our gate classes so that each togate can choose the
    # proper input line for the connection.


#The following fragment constructs the circuit shown earlier in the section:
# (after adding connector)

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1,g3)
c2 = Connector(g2,g3)
c3 = Connector(g3,g4)


# code from book:

class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getName()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())

main()

'''
Self Check
Create a two new gate classes, one called NorGate the other called NandGate.
NandGates work like AndGates that have a Not attached to the output.
NorGates work lake OrGates that have a Not attached to the output.

Create a series of gates that prove the following equality NOT (( A and B) or (C and D))
is that same as NOT( A and B ) and NOT (C and D). Make sure to use some of your new gates in the simulation.
'''

# solution: utilize inheritance:
# seems to be some sort of issue with using super (again, instructor using python 3)

class NandGate(AndGate):

    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

class NorGate(OrGate):

    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


