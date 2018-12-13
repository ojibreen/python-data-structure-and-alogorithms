# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:04:48 2018

@author: oJibreen
"""

class BinarySearch:
        
    def search(self, arr, x, left, right):
        if left > right:
            return False
        
        mid = int((left + right) / 2)
        if arr[mid] == x:
            return True
        elif x < arr[mid]:
            return self.search(arr, x, left, mid - 1)
        else:
            return self.search(arr, x, mid + 1, right)