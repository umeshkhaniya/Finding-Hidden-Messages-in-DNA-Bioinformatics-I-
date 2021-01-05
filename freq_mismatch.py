
# Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
# Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
# Output: All most frequent k-mers with up to d mismatches in Text.

#Code Challenge: Solve the Frequent Words with Mismatches Problem.

def FrequentWordsWithMismatches(Text, k, d):
	Patterns = []
	frequency_mis = {}
	for i in range(len(Text) - k +1):
		if Text[i:i+k] not in frequency_mis:
			frequency_mis[Text[i:i+k]] = 1
		else:
			frequency_mis[Text[i:i+k]] += 1
	return frequency_mis




def Neighbors(Pattern, d):
	if d = 0:
		return Pattern
	if 




Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1
print(FrequentWordsWithMismatches(Text, k, d))