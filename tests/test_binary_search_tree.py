# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 18:47:56 2018

@author: oJibreen
"""

from structures.trees import BinarySearchTree


class TestBinarySearchTree:
    
    def test_insert_node(self):
        bst = BinarySearchTree(13)
        assert bst.value == 13
        
        bst.insertNode(4)
        bst.insertNode(3)
        assert bst.leftChild.value == 4
        assert bst.leftChild.leftChild.value == 3
        
        bst.insertNode(14)
        bst.insertNode(19)
        assert bst.rightChild.value == 14
        assert bst.rightChild.rightChild.value == 19
        
    def test_find(self):
        bst = BinarySearchTree(1001)
        bst.insertNode(15)
        bst.insertNode(133)
        bst.insertNode(1)
        bst.insertNode(1000)

        assert bst.find(15) == True
        assert bst.find(133) == True
        assert bst.find(1) == True
        assert bst.find(1000) == True
        assert bst.find(1001) == True
        
        assert bst.find(11) == False
        assert bst.find(4000) == False
        
    def test_find_minimum_value(self):
        bst = BinarySearchTree(50)
        bst.insertNode(54)
        bst.insertNode(75)
        bst.insertNode(31)
        bst.insertNode(1)
        
        assert bst.findMinimumValue() == 1
        
    def test_remove_node(self):
        bst = BinarySearchTree(15)
        bst.insertNode(10)
        bst.insertNode(8)
        bst.insertNode(12)
        bst.insertNode(20)
        bst.insertNode(17)
        bst.insertNode(25)
        bst.insertNode(19)
        
        assert bst.find(8) == True
        assert bst.removeNode(8, None) == True
        assert bst.find(8) == False
        
        assert bst.find(17) == True
        assert bst.removeNode(17, None) == True
        assert bst.find(17) == False
        
        assert bst.find(15) == True
        assert bst.removeNode(15, None) == True
        assert bst.find(15) == False
       
        
        