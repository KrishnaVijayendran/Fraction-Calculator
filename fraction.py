def myGcd(a, b):
	if b > a: a, b = b, a
	while b != 0:
	   t = b
	   b = a % b
	   a = t
	return a

def lcm(a, b):
	result = a*b/myGcd(a,b)
	return int(result)

class Fraction(object):

	def __init__(self, num, denom):
		if denom == 0:
			raise ZeroDivisionError
		if denom<0 and num>0:
			denom = abs(denom)
			num = (-1*num)
		elif denom<0 and num<0:
			denom = abs(denom)
			num = abs(num)
		#reduce the fraction	
		gcd = myGcd(abs(num), abs(denom))
		self.num = num // gcd
		self.denom = denom // gcd

		#replaced __str__ with __repr__, its more effective
	def __repr__(self):
		if self.denom == 1: return str(self.num)
		#number over itself
		elif self.denom == self.num: return str(1)
		return str(self.num) + '/' + str(self.denom)

	def __eq__(self, other):
		return self.num == other.num and self.denom == other.denom

	def __lt__(self, other):
		if self.num * other.denom < other.num * self.denom:
			return True
		else:
			return False
	
	def multiply(self, other):
		num = self.num * other.num
		denom = self.denom * other.denom
		return Fraction(num, denom)
	
	def add(self, other):
		multiple = lcm(self.denom, other.denom)
		newNum = self.num * (multiple//self.denom) + (multiple//other.denom) * other.num
		return Fraction(newNum, multiple)

	def subtract(self, other):
		multiple = lcm(self.denom, other.denom)
		newNum = self.num * (multiple//self.denom) - (multiple//other.denom) * other.num
		return Fraction(newNum, multiple)
	
	def divide(self, other):
		newNum = self.num * other.denom
		newDenom = self.denom * other.num
		return Fraction(newNum, newDenom)
		
	def absValue(self):
		return Fraction(abs(self.num), abs(self.denom))
		
	def negate(self):
		return Fraction(self.num * -1, self.denom)