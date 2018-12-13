# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 19:30:45 2018

@author: oJibreen
"""

from structures.stacks import Stack

class TestStack:
    def test_stack(self):
        s = Stack()
        assert s.isEmpty() == True
        assert s.size() == 0
        assert s.peak() == None
        
        s.push(1)
        s.push(2)
        s.push(3)
        assert s.isEmpty() == False
        assert s.pop() == 3
        assert s.size() == 2
        assert s.peak() == 2
        
        s.push('foo')
        assert s.peak() == 'foo'
        assert s.size() == 3
        
        s.pop()
        assert s.peak() == 2
        assert s.size() == 2
        
        # Pop remaining items.
        s.pop()
        s.pop()
        assert s.isEmpty() == True
        assert s.size() == 0
        assert s.pop() == None
        assert s.peak() == None
        
