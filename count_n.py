# Our goal now is to modify our previous algorithm for the Frequent Words Problem 
# in order to find DnaA boxes by identifying frequent k-mers, possibly with mismatches. 
# Given strings Text and Pattern as well as an integer d, we define Countd(Text, Pattern) as the 
# total number of occurrences of Pattern in Text with at most d mismatches. 
# For example, Count1(AACAAGCTGATAAACATTTAAAGAG, AAAAA) = 4 because AAAAA appears four times in this string
#  with at most one mismatch: AACAA, ATAAA, AAACA, and AAAGA. Note that two of these occurrences overlap.

# Exercise Break: Compute Count2(AACAAGCTGATAAACATTTAAAGAG, AAAAA).

def Count_n(Text, Pattern, n):
	result = 0
	count = 0
	for i in range(len(Text) - len(Pattern) + 1):
		for j , nuc in enumerate(Text[i: i + len(Pattern)]):
			if nuc != Pattern[j]:
				count += 1

		if count <= n:
			result += 1
		count = 0
	return result


Text = 'CATGCCATTCGCATTGTCCCAGTGA'
Pattern = 'CCC'
n = 2

print(Count_n(Text, Pattern, n))
