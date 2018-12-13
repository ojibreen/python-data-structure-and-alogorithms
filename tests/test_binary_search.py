from search import BinarySearch


class TestBinarySearch:
	def test_binary_search(self):
		binarySearch = BinarySearch()

		l = [3,4,5,6,13,101,300,67,48]
		l.sort()
		assert binarySearch.search(l, 300, 0, len(l) - 1) == True
		assert binarySearch.search(l, 1000, 0, len(l) - 1) == False
		assert binarySearch.search(l, 67, 0, len(l) - 1) == True
		assert binarySearch.search(l, -1, 0, len(l) - 1) == False

