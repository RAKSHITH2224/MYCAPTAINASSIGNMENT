'''
Write Python code to create a function called most_frequent that takes a 
string and prints the letters in decreasing order of frequency.
Use dictionaries.
'''

#sir i tried to arrange them in decreasing order but i got some errors while sorting



def most_frequent(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] = dict[n] + 1
        else:
            dict[n] = 1
    return dict
print(most_frequent('virupakshappa')) 
