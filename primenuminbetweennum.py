first = int(input('Enter first number '))
second = int(input('Enter second number '))
print("Prime numbers between", first, "and", second, "are:")
for num in range(lower, upper + 1):
	if num > 1:
		for i in range(2, num):
			if (num % i) == 0:
				break
		else:
			print(num)