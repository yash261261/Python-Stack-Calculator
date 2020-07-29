import re

class Calculator:
	"""
	This is a stack-based calculator
	Implemements: addition, subtraction, division, multiplication
	"""
	def __init__(self):
		self._stack = []
		self._vars = dict()

	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		result = 0
		current = 0
		sign = 1
		stack = []
		for ss in s:
			if ss.isdigit():
				current = int(ss) + 10*current
			elif ss in ["-", "+"]:
				result += sign*current
				current = 0
				if ss == "+":
					sign = 1
				else:
					sign = -1

			elif ss == "(":
				stack.append(result)
				stack.append(sign)
				sign = 1
				result = 0
			elif ss == ")":
				result += sign * current
				result *= stack.pop()
				result += stack.pop()
				current = 0
		return result + current * sign

print("Launching the calculator...")
calc = Calculator()
status = False # Boolean?
user_input = ""
while user_input not in ["exit", "stop", "quit", "close"]:
	regex = re.search('[a-zA-Z]', user_input)
	if regex != None:
		print("Please write an expression.")
	expression = ""
	user_input = input("> ")
	output = calc.calculate(user_input)
	print(output)
	# for loop here?
print("Closing the calculator...")
print(expression)
