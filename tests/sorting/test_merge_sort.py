'''
Author: ojibreen
Date: 12/25/18
'''

from sorting.merge_sort import _merge
from sorting.merge_sort import _split
from sorting.merge_sort import sort


class TestMergeSort:
    def test_split(self):
        arr = [5,1,8,3,2]
        a, b = _split(arr)
        assert len(a) == 2
        assert len(b) == 3

        arr = [5, 1, 8, 3]
        a, b = _split(arr)
        assert len(a) == 2
        assert len(b) == 2


    def test_merge(self):
        a = [3, 4, 5]
        b = [1, 2]
        m = _merge(a, b)
        assert len(m) == 5
        for n in range(1, 6):
            assert m[n - 1] == n

        a = [1, 2]
        b = [3, 4]
        m = _merge(a, b)
        assert len(m) == 4
        for n in range(1, 5):
            assert m[n - 1] == n

    def test_merge_sort(self):
        a = [4,11,1,2,7,5,6,8,9,3,10]
        b = sort(a)
        assert len(b) == 11
        for i in range(1, 11):
            assert b[i - 1] == i