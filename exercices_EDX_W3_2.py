# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 22:11:05 2020

@author: Sam
"""


import os 
import pandas as pd 
import numpy as np 
from collections import Counter


def count_words_fast(text): 
    text = text.lower() 
    skips = [".", ",", ";", ":", "'", '"', "\n", "!", "?", "(", ")"] 
    for ch in skips: 
        text = text.replace(ch, "") 
    word_counts = Counter(text.split(" ")) 
    return word_counts

def word_stats(word_counts): 
    num_unique = len(word_counts) 
    counts = word_counts.values() 
    return (num_unique, counts)



# Exercice 1
    
hamlets = pd.read_csv("hamlets.csv", index_col=0)
#print(hamlets)


# Exercice 2

language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)

data = pd.DataFrame(columns = ("word", "count"))

word_number = 1
for word in counted_text:
    data.loc[word_number] = word, counted_text[word]
    word_number += 1

#print(data)
#print(counted_text["hamlet"])

# Exercice 3

data = pd.DataFrame(columns = ("word", "count", "length", "frequency"))

word_number = 1
frequent_count = 0
infrequent_count = 0
unique_count = 0
frequent_mean = 0
infrequent_mean = 0
unique_mean = 0
for word in counted_text:
    if counted_text[word] > 10:
        data.loc[word_number] = word, counted_text[word], len(word), "frequent"
        frequent_count += 1
        frequent_mean += len(word)
    if 1 < counted_text[word] <= 10:
        data.loc[word_number] = word, counted_text[word], len(word), "infrequent" 
        infrequent_count += 1
        infrequent_mean += len(word)
    if counted_text[word] == 1:
        data.loc[word_number] = word, counted_text[word], len(word), "unique"
        unique_count += 1
        unique_mean += len(word)
    word_number += 1

frequent_mean = frequent_mean / frequent_count
infrequent_mean = infrequent_mean / infrequent_count
unique_mean = unique_mean / unique_count
    
#print(data)
#print(unique_count)


# Exercice 4

sub_data = pd.DataFrame(columns = ("language", "frequency", "mean_word_length", "num_words"))

value_number = 1
frequency = ["frequent", "infrequent", "unique"]
for value in frequency:
    if value == "frequent":
        sub_data.loc[value_number] = language, value, frequent_mean, frequent_count
    if value == "infrequent":
        sub_data.loc[value_number] = language, value, infrequent_mean, infrequent_count
    if value == "unique":
        sub_data.loc[value_number] = language, value, unique_mean, unique_count
    value_number += 1

#print(sub_data)


# Exercice 5

def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })
    
    data.loc[data["count"] > 10,  "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1,  "frequency"] = "unique"
    
    data["length"] = data["word"].apply(len)
    
    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })
    
    return(sub_data)
    
"""
    grouped_data = pd.DataFrame({
        summarize_text(language, text)
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })
"""


