from fraction import *
import re

currentValue = 0
rememberedOperator = None

def main():
	global currentValue
	print("Welcome to fractions calculator by Krishna and Kishin\n")
	while(True):
		print(currentValue)
		typedInput = input("Enter input: ")
		currentValue = evaluate(0, typedInput)
		
def evaluate(fraction, inputString):
	global rememberedOperator
	global currentValue
	newList = stringToFractions(inputString)
	checkRememberedOperator(newList)
	for i in range(0, len(newList)):
		try: 
			if not isinstance(newList[i], Fraction) and newList[i] == '+':
				currentValue = currentValue.add(newList[i+1])
			if not isinstance(newList[i], Fraction) and newList[i] == '-':
				currentValue = currentValue.subtract(newList[i+1])
			if not isinstance(newList[i], Fraction) and newList[i] == '*':
				currentValue = currentValue.multiply(newList[i+1])
			if not isinstance(newList[i], Fraction) and newList[i] == '/':
				currentValue = currentValue.divide(newList[i+1])
		except IndexError:
			if newList[i] == '+' or newList[i] == '-' or newList[i] == '/' or newList[i] == '*':
				rememberedOperator = newList[i]
	return currentValue

def checkRememberedOperator(newList):
	'''Checks to see if an operation was stored. If one was stored, we use the operator to operate on the first element in the list and the currentValue stored by the calculator. If none was stored, we start again. If one was stored and another operator was entered an error is raised.	
	'''
	global rememberedOperator
	global currentValue
	if rememberedOperator != None and not isinstance(newList[0], Fraction) and \
				(newList[0] == '+' or newList[0] == '-' or newList[0] == '/' or newList[0] == '*'):
		raise ValueError("You already had an operator stored!")
	elif rememberedOperator != None:
		if rememberedOperator == '+':
			currentValue = currentValue.add(newList[0])
		elif rememberedOperator == '/':
			currentValue = currentValue.divide(newList[0])
		elif rememberedOperator == '-':
			currentValue = currentValue.subtract(newList[0])
		elif rememberedOperator == '*':
			currentValue = currentValue.multiply(newList[0])		
		rememberedOperator = None
	elif isinstance(newList[0], Fraction):
		currentValue = newList[0]

def checkWords():
	#check negate
	#check absolute value
	#check clear
	pass

def stringToFractions(inputString):
	'''Takes the input string and converts all the fractions (2/3) to Fraction objects. All individual numbers (i.e. 2 4 5) are converted to fraction objects with a denominator of 1.'''
	inputString = inputString.split()
	for i in range(0, len(inputString)):
		frac = re.match(r"(-*\d+)/(-*\d+)", inputString[i])
		singleNumber = re.match(r"(-*\d+)", inputString[i])
		if frac:
			inputString[i] = Fraction(int(frac.group(1)), int(frac.group(2)))
		elif singleNumber:
			inputString[i] = Fraction(int(singleNumber.group(1)), 1)
	return inputString

main()	