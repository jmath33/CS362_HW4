import unittest
import name_gen

class testNameGen(unittest.TestCase):

	def test_name(self):
		self.assertEqual(name_gen.name("John", "Doe"), "John Doe")

	def test_name_2(self):
		self.assertEqual(name_gen.name('D', 'M'), "D M")

	def test_name_3(self):
		self.assertEqual(name_gen.name("Squirrel", 's'), "Squirrels");

if __name__ == '__main__':
	unittest.main()
