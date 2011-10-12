from FractionCalculator import *
from fraction import *
import unittest

class FractionCalculatorTest(unittest.TestCase):	
	def TestStringToFractions(self):
		self.assertEqual( [2/3, '+', 4/3, '-', 2, '*', 1, 1, -9/2] , FractionCalculator.stringToFractions("2/3 + 4/3 - 2 * 1 -9/-9 9/-2"))

unittest.main()		

#	self.assertEqual([2/3, 4/3, 2, 1, 1, -9/2], stringToFractions("2/3 4/3 2 1 -9/-9 9/-2"))
