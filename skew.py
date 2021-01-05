def Skew(genome):
	result = [0] * (len(genome) + 1)
	for i in range(len(genome)):
		if genome[i] == 'G':
			result[i+1] = result[i] + 1
		elif genome[i] == 'C':
			result[i+1] = result[i] - 1
		else:
			result[i+1] = result[i] 

	return result, ' '.join(str(x) for x in result)



genome = 'CATTCCAGTACTTCGATGATGGCGTGAAGA'
def min_Skew():
	min_skew = []
	skew_lst = Skew(genome)[0]
	for i in range(len(skew_lst)):
		if skew_lst[i] == min(skew_lst):
			min_skew.append(i)
	return ' '.join(str(x) for x in min_skew)


print(min_Skew())