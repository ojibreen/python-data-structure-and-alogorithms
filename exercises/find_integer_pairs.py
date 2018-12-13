# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:44:09 2018

@author: oJibreen
Description: Given an array of integers and a total, this function will search the
array to find two numbers that sum to equal the total (if they exist).  This function runs in
O(n) time complexity.
"""

def findPair(arr, total):
    compliments = {}
    for n in  arr:
        compliment = total - n
        if n in compliments:
            return (compliment, n)
        else:
            compliments[compliment] = compliment
    return None
