"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""

sum = 0

# for the natural numbers starting from 0 and less than 1000
for x in range(0,1000):
	# check if divisible by 3 or 5
	if x % 3 == 0 or x % 5 == 0:
		# if so, add to the total sum 
		sum += x
		
	#check the next number
	x += 1

# print the sum of all the multiples
print sum