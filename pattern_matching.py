#ask for the list
def PatternMatching(Pattern, Genome):
    start_point = []
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i: i + len(Pattern)] == Pattern:
            start_point.append(i)
    # sorted
    sorted(start_point)
    return ' '.join(str(x) for x in start_point)
    #return sorted(start_point)

Pattern = 'CTTGATCAT'

print(PatternMatching(Pattern, Genome))
