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
"""
list_message = []
for i in range(len(message)):
        list_message.append(alphabet[position[message[i]] + 1])

encoded_message = ''.join(list_message)

print(encoded_message)
"""

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
print(encoded_message)

decoded_message = encoding(encoded_message, -3)
print(decoded_message)




"""
inputfile = "python_case_studies/translation/dna_NM_207618.2.txt"
f = open(inputfile, "r")
seq = f.read()
seq = seq.replace("\n", "")
seq = seq.replace("\r", "")
print(seq[40:50])


table = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

#print(table["GCC"])
"""
