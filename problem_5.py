"""What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

x = 1
for y in (range(1, 21)):
    if x % y > 0:
        for z in range(1, 21):
            if (x*z) % y == 0:
                x *= z
                break
print x

# Answer = 232792560