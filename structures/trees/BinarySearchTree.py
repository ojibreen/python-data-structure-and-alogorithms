# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 18:24:51 2018

@author: oJibreen
"""

class BinarySearchTree:
    
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        
    def insertNode(self, value):
        
        if value <= self.value and self.leftChild:
            self.leftChild.insertNode(value)
        
        elif value <= self.value:
            self.leftChild = BinarySearchTree(value)
        
        elif value >= self.value and self.rightChild:
            self.rightChild.insertNode(value)
        
        else:
            self.rightChild = BinarySearchTree(value)
            
    def find(self, value):
        if value < self.value and self.leftChild:
            return self.leftChild.find(value)
        
        elif value > self.value and self.rightChild:
            return self.rightChild.find(value)
        
        return value == self.value
    
    def removeNode(self, value, parent):
        if value < self.value and self.leftChild:
            return self.leftChild.removeNode(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.rightChild:
            return self.rightChild.removeNode(value, self)
        elif value > self.value:
            return False
        else:
            if self.leftChild is None and self.rightChild is None and self == parent.leftChild:
                parent.leftChild = None
                self.clearNode()
            elif self.leftChild is None and self.rightChild is None and self == parent.rightChild:
                parent.rightChild = None
                self.clearNode()
            elif self.leftChild and self.rightChild is None and self == parent.leftChild:
                parent.leftChild = self.leftChild
                self.clearNode()
            elif self.leftChild and self.rightChild is None and self == parent.rightChild:
                parent.rightChild = self.leftChild
                self.clearNode()
            elif self.rightChild and self.leftChild is None and self == parent.leftChild:
                parent.leftChild = self.rightChild
                self.clearNode()
            elif self.rightChild and self.leftChild is None and self == parent.rightChild:
                parent.rightChild = self.rightChild
                self.clearNode()
            else:
                self.value = self.rightChild.findMinimumValue()
                self.rightChild.removeNode(self.value, self)

        return True
    
    def clearNode(self):
        self.value = None
        self.leftChild = None
        self.rightChild = None
    
    def findMinimumValue(self):
        if self.leftChild:
            return self.leftChild.findMinimumValue()
        else:
            return self.value