import random

def get_lucky_nums():
	return random.sample(range(1,46), 6)

if __name__ == '__main__':
	times = int(input('Enter nums(1-100): '))
	for _ in range(times):
		print(get_lucky_nums())
