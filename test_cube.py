import unittest
import cube
import math

class testCube(unittest.TestCase):

	def test_volume(self):
		self.assertEqual(cube.volume(math.pi,4,math.sqrt(25)), 62.8318530718)

	def test_volume_2(self):
		self.assertEqual(cube.volume(5.5,6,7.0), 231)	

	def test_volume_3(self):
		self.assertEqual(cube.volume(-1,-3,-12), -36)

if __name__ == '__main__':
	unittest.main()
