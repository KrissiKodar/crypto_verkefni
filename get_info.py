import requests
import bs4 as bs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# funtion that returns words and their frequency
def get_word_freq(words):
    word_freq = {}
    for w in words:
        if w in word_freq:
            word_freq[w] += 1
        else:
            word_freq[w] = 1
    return word_freq

# function that takes a url and returns a dictionary of words and their frequency
def get_info(url):
    resp = requests.get(url)
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    words = soup.text.split()
    word_freq = get_word_freq(words)
    # sort the dictionary by value
    word_freq = {k: v for k, v in sorted(word_freq.items(), key=lambda item: item[1], reverse=True)}
    return word_freq


L = get_info('https://en.wikipedia.org/wiki/Bir_Hakeim_rescue')

print(L)

# histogram of 10 most frequent words
plt.bar(list(L.keys())[:10], list(L.values())[:10], color='g')
plt.show()
    
    