for j in range(1, 16+1):
	if j%3==0 or j%5==0:
		print('fizz'*(j%3==0)+'buzz'*(j%5==0))
	else:
		print(f'{j}')
