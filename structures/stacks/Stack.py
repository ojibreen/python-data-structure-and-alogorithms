# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 19:18:44 2018

@author: oJibreen

NOTES:
    This implementation uses pop() and append() methods of Python's list data structure, as they run
    in O(1).  Other methods of the list data structures, such as pop(0), run in O(n), and could
    impact the performence of the stack when given large inputs.
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()
        
    def peak(self):
        if self.size() == 0:
            return None
        return self.items[len(self.items) - 1]
        
    def size(self):
        return len(self.items)