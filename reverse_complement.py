Pattern = 'ATGCAA'
result = ''
for i in Pattern:
	if i == "A":
		result = "T" + result
	if i == "T":
		result = "A" + result 
	if i == "C":
		result = "G" + result
	if i == "G":
		result = "C" + result  

print(result)