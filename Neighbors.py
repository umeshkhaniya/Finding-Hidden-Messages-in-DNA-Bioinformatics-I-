# Code Challenge: Implement Neighbors to find the d-neighborhood of a string.

# Input: A string Pattern and an integer d.
# Output: The collection of strings Neighbors(Pattern, d). 
# (You may return the strings in any order, but each line should contain only one string.)

def Neighbors(Pattern, d):
	if d == 0:
		return {Pattern}
	if len(Pattern) == 1:
		return {'A', 'C', 'G', 'T'} #return set
	Neighborhood = set()
	SuffixNeighbors = Neighbors(suffix(Pattern), d)

	for text in 


Pattern = "AGT"
d = 4

def suffix(Pattern):
	suffix = Pattern[1: len(Pattern)]
	return suffix



def HammigDistance(p,q):
	hamming = 0
	for i in range(len(p)):
		if p[i] != q[i]:
			hamming += 1
	return hamming

print(Neighbors(Pattern, d)) 