
from exercises.find_integer_pairs import findPair

class TestFindIntegerPairs:
	def test_find_integer_pairs(self):
		l = [1,6,5,4,300,12,13,5,7,-1,0]
		sum = 7
		answer = findPair(l, sum)
		assert answer == (1,6)

		sum = 304
		answer = findPair(l, sum)
		assert answer == (4,300)

		sum = 1000
		answer = findPair(l, sum)
		assert answer == None

		sum = 5
		answer = findPair(l, sum)
		assert answer == (1,4)