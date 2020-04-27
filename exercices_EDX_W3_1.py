# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:35:18 2020

@author: Sam
"""


# Exercice 1

import string

alphabet = ' ' + string.ascii_lowercase

#print(alphabet)

# Exercice 2
position = {}

for i in range(len(alphabet)):
    position[alphabet[i]] = i
    
#print(position)


# Exercice 3
    
message = "hi my name is caesar"

list_message = []
for i in range(len(message)):
        list_message.append(alphabet[position[message[i]] + 1])

encoded_message = ''.join(list_message)

#print(encoded_message)


# Exercice 4

def encoding(message, key):
    list_message = []
    encoded_message = ''
    for i in range(len(message)):
        if position[message[i]] + key > 26:
            key = key - 27

        list_message.append(alphabet[position[message[i]] + key])

    encoded_message = ''.join(list_message)
    return encoded_message

encoded_message = encoding(message, 3)
#print(encoded_message)

decoded_message = encoding(encoded_message, -3)
#print(decoded_message)