import unittest
import avg

list1 = [1, 2, 3]

list2 = []

list3 = [3*4, 2+3, "three"]

class testAvg(unittest.TestCase):

	def test_avg(self):
		self.assertEqual(avg.avg(list1), 2)

	def test_avg_1(self):
		self.assertEqual(avg.avg(list2), 0)

	def test_avg_2(self):
		self.assertEqual(avg.avg(list3), 5.66)

if __name__ == '__main__':
	unittest.main()
