for j in range(1, 16+1):
	if j%15==0:
		print('fizzbuzz')
	elif j%3==0:
		print('fizz')
	elif j%5==0:
		print('buzz')
	else:
		print(f'{j}')
