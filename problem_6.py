"""Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""


#square of sums
b = 0
for a in range(1, 101):

	b += a
print "Square of sums", b * b

#sum of squares

d = 0
for c in range (1, 101):
	d += c * c
print "Sum of squares:", d

print "Difference:", (b * b) - d

# Answer: 25164150