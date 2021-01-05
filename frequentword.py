def FrequentWords(Text,k):
	FrequentPatterns = {}

	for i in range(len(Text) - k +1):
		if Text[i: i+ k] not in FrequentPatterns:
			FrequentPatterns[Text[i: i+ k]] = 1
		else:
			FrequentPatterns[Text[i: i+ k]] += 1

	max_count = max(FrequentPatterns.values())
	max_pattern = []
	for j in FrequentPatterns:
		if FrequentPatterns[j] == max_count:
			max_pattern.append(j)
	return ' '.join(max_pattern)
Text = 'CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT'
k = 3
print(FrequentWords(Text,k))

# need to print answer like this: CAGGAGACTAAAT AGGAGACTAAATG
# FrequentPatterns = {}

# for i in range(len(Text) - k +1):
# 	if Text[i: i+ k] not in FrequentPatterns:
# 		FrequentPatterns[Text[i: i+ k]] = 1
# 	else:
# 		FrequentPatterns[Text[i: i+ k]] += 1

# max_count = max(FrequentPatterns.values())
# max_pattern = []
# #print(max_count)
# #print(FrequentPatterns)
# for j in FrequentPatterns:
# 	if FrequentPatterns[j] == max_count:
# 		max_pattern.append(j)
		
# print(' '.join(max_pattern))
