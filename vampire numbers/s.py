import itertools as it

# Time O(N! * N) | Mem O(N)
def getFangs(num_str: str) -> None | tuple:
	num_iter: Iterator = it.permutations(num_str, len(num_str))

	for num_tuple in num_iter:
		x, y = num_tuple[:int(len(num_tuple)/2)], num_tuple[int(len(num_tuple)/2):]
		x_str, y_str = ''.join(x), ''.join(y)
		if x_str[-1] == '0' and y_str[-1] == '0':
			continue

		if int(x_str) * int(y_str) == int(num_str):
			return x_str, y_str

	return None

def isVampire(m_int) -> bool:
	n_str: str = str(m_int)

	if len(n_str) % 2 == 1:
		return False

	return getFangs(n_str) != None

print(isVampire(536_539)) # True
print(isVampire(1234)) # False
