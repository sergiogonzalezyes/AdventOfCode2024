#NOTE  DAY 2 PART 1

with open('day2/inputday2.txt', 'r') as file:
        report = [list(map(int, line.split())) for line in file]

#NOTE LOGIC
safe_reports = 0
safe = None


for line in report:
        sortedAsc = sorted(line)
        sortedDesc = sorted(line, reverse=True)
        if line != sortedAsc and line != sortedDesc:
                continue
        elif len(line) != len(set(line)):
                continue
        else: 
                for index, level in enumerate(range(len(line) - 1), 1):
                        val = line[index]
                        difference = val - line[index - 1]
                        
                        if abs(difference) > 3 or abs(difference) < 1:
                                safe = False
                                break
                        else:
                                safe = True

                if safe:
                        safe_reports += 1
                else:
                        continue

print('number of safe reports: ', safe_reports)