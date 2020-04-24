# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:10:42 2020

@author: Sam
"""

##--------------------------------##
#Exercice  1

import string

alphabet = string.ascii_letters

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}
# write your code here!

"""
for i in range(len(sentence)):
    if sentence[i] in count_letters:
        count_letters[sentence[i]] += 1
    else:
        count_letters[sentence[i]] = 1
"""

def counter(input_string):

    alphabet = string.ascii_letters
    
    for i in range(len(input_string)):
        if input_string[i] in alphabet:
            if input_string[i] in count_letters:
                count_letters[input_string[i]] += 1
            else:
                count_letters[input_string[i]] = 1
    return count_letters

#print(counter(sentence))

address = """Four score and seven years ago our fathers brought forth on this continent, a new nation, 
conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a 
great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. 
We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final 
resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper 
that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- 
this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add 
or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. 
It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so 
nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored 
dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here 
highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of 
freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."""   

address_count = counter(address)

#print(address_count)

count_letters_max = max(address_count, key=address_count.get)
#print(count_letters_max)


##--------------------------------##
#Excercie  2

import math

#print(math.pi/4)

import random

random.seed(1) # Fixes the see of the random number generator.

def rand():
   return random.uniform(-1, 1)

rand()



def distance(x, y):
    diff_x = y[0]-x[0]
    diff_y = y[1]-x[1]
 
    distance = math.sqrt(diff_x**2 + diff_y**2)

    return distance

x=(0,0)
y=(1,1)

distance(x, y)


def in_circle(x, origin = [0,0]):
    radius = distance(x, origin)
    if radius < 1:
        return True
    else:
        return False

in_circle((1,1))



random.seed(1)
R=10000
inside = []
count_true = 0
for i in range(R):
    point = in_circle((rand(),rand()))
    inside.append(point)
    if point:
        count_true += 1

#print(count_true / R)

difference = (math.pi / 4) - (count_true / R)

#print(difference)



##--------------------------------##
# Exercice 3
"""
def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    return [sum(x[i:(i+width)]) / width for i in range(n)]

x = [0,10,5,3,1,5]
#print(sum(moving_window_average(x, 1)))
"""

def moving_window_average(x, n_neighbors=1):
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    n = len(x)
    
    list_x=[]
    for i in range(n_neighbors,n-n_neighbors):
        sum_x=0
        for j in range(-n_neighbors, n_neighbors+1):
            sum_x = sum_x + x[i+j]
        mean = sum_x / width
        list_x.append(mean)
    
    return list_x


x = [0,10,5,3,1,5]
print(moving_window_average(x, 1))
print(sum(moving_window_average(x, 1)))

"""
R = 1000
Y = []
x = []
ranges = []
random.seed(1)
for i in range(R):
    x.append(random.uniform(0,1))

for i in range(1, 10):
    Y.append(moving_window_average(x, i))

for i in range(9):
    ranges.append(max(Y[i])-min(Y[i]))


#print(Y[5][9])
#print(ranges)
"""











