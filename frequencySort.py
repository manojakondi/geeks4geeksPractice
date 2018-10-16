"""
Given an array containing integers, in which the elements are repeated multiple times.
Now sort the array wrt the frequency of numbers.
"""

from collections import Counter

list = [1,2,3,4,3,3,3,6,7,1,1,9,3,2]

print(list)

counts = Counter(list)

print(counts)

newList = sorted(list, key=counts.get, reverse=True)

print(newList)
