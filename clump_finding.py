# Clump Finding Problem: Find patterns forming clumps in a string.

# Input: A string Genome, and integers k, L, and t.
# length of k_mers: pattern length: k: k_mers, length of clump : L and t is t times appear in clump of length L
# Output: All distinct k-mers forming (L, t)-clumps in Genome.
#def ClumpFinding(genome, k, L,t):
# def ClumpFinding(genome, k, L, t):
# 	frq_dict = {}
# 	clumps = []
# 	for i in range(0, len(genome) - k +1):
# 		if genome[i: i + k]  in frq_dict:
# 			frq_dict[genome[i: i + k]].append(i)
# 		else:
# 			frq_dict[genome[i: i + k]] = [i]
# 	#return frq_dict
# 	for pat in frq_dict:
# 		if len(frq_dict[pat]) == t:
# 			for x in range(len(frq_dict[pat])):
# 				if frq_dict[pat][t-1] - frq_dict[pat][0] + k+ 1 <= L:
# 					if pat not in clumps:
# 						clumps.append(pat)

# 					#print(frq_dict)
					
		
# 	# 	if 	len(frq_dict[pat]) > t:
# 	# 		for x in range(len(frq_dict[pat]) - t + 1):
# 	# 			if frq_dict[pat][x+t -1] - frq_dict[pat][x] + k <= L and  frq_dict[pat][x+t] - frq_dict[pat][x] + k  > L:
# 	# 				if pat not in clumps:

# 	# 					clumps.append(pat)
# 	#return ' '.join(str(x) for x in clumps)
# 	return frq_dict


# lets find the frequency match that is how many times that pattern appear

def 

genome = 'AAAACGTCGAAAAA'
k = 2
L = 4
t = 2

print(ClumpFinding(genome, k, L, t))

