"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

palindromelist = []

def palindrome(number):
	if number[0] == number[5] and number[1] == number[4] and number[2] == number[3]:
		return True
	else:
		return False
		

for a in range(880, 999):
	b = 999
	while b > 800:
		product = str(a * b)
		if palindrome(product):
			print a, "times", b, "equals", product
			palindromelist.append(product)
		b -= 1
	
print "Largest: ", max(palindromelist)

# Answer: 906609