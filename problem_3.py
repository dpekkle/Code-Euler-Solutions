"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?"""

def primefactors(number):
	factors = [1]
	n = 2

	while n <= number:
		if number%n==0:
			factors.append(n)
			number /= n
		
		else:
			n += 1
	return factors	
	
x = primefactors(600851475143)

Answer = 1
for i in x:
	Answer *= i
	
print "The prime factors of %d are: %s" % (Answer, x)
