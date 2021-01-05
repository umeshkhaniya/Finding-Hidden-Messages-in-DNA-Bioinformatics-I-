def PatternCount(text, pattern):
	count = 0
	for i in range(len(text) - len(pattern) +1):
		if text[i: i +len(pattern)] == pattern:
			count += 1
	return count

pattern = 'CGCG'
text = 'CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC'

print(PatternCount(text, pattern))

# This will read the file and give text and pattern based on the line.

def PatternCount(input):
	list_file = []
	with open(input, "r") as inputfile:
		read_line = inputfile.readlines()
		for x in read_line:
			list_file.append(x.strip().split())
	count = 0
	text = list_file[0][0]
	pattern = list_file[1][0]
	count = 0
	for i in range(len(text) - len(pattern) +1):
		if text[i: i +len(pattern)] == pattern:
			count += 1
	return count

	
print(PatternCount("dataset_2_7.txt"))
