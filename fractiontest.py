import unittest
from fraction import *


class FractionTest(unittest.TestCase):

	def testZeroDivide(self):
		# Notice that assertRaises does not call Fraction directly!
		self.assertRaises(ZeroDivisionError, Fraction, 1, 0)
		
	def testMultiply(self):
		self.assertEqual(Fraction(3, 10),
						 Fraction(1, 2).multiply(Fraction(3, 5)))

	def testLessThan(self):
		self.assertTrue(Fraction(1, 100) < Fraction(1, 2))

	def testEqual(self):
		self.assertEqual(Fraction(1, 2), Fraction(1, 2))
		self.assertEqual(Fraction(1, 2), Fraction(3, 6))
		self.assertEqual(Fraction(-1, 2), Fraction(1, -2))
		self.assertEqual(Fraction(-1, -2), Fraction(1, 2))

	def testAdd(self):
 		self.assertEqual(Fraction(1,2), Fraction(1,3).add(Fraction(1,6)))

	def testSubtract(self):
		self.assertEqual(Fraction(1,6), Fraction(1,3).subtract(Fraction(1,6)))
 		
	def testDivide(self):
		self.assertEqual(Fraction(48,13), Fraction(12,13).divide(Fraction(1,4)))
		
	def testAbsValue(self):
		self.assertEqual(Fraction(12,13), Fraction(-12,13).absValue())
		self.assertEqual(Fraction(12,13), Fraction(12,13).absValue())
		self.assertEqual(Fraction(12,13), Fraction(-12,-13).absValue())
		
	def testNegate(self):
		self.assertEqual(Fraction(12,13), Fraction(-12,13).negate())
		self.assertEqual(Fraction(-12,13), Fraction(12,13).negate())
		self.assertEqual(Fraction(-12,13), Fraction(-12,-13).negate())
 				
unittest.main()
