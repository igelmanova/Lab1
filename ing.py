line = str(input())
if 'ing' in line:
    line = line+"ly"
    print(line)
elif len(line) >= 3:
    line = line+"ing"
    print(line)
else:
    print(line)
