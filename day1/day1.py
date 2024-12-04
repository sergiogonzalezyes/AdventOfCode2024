list1ex = [3, 4, 2, 1, 3, 3]
list2ex = [4, 3, 5, 3, 9, 3]


# list1 = []
# list2 = []

# import csv

# with open('day1/list_1.csv', 'r') as file:
#     csv_reader = csv.reader(file)

#     for row in csv_reader:
#         list1.append(int(row[0]))

# with open('day1/list_2.csv', 'r') as file:
#     csv_reader = csv.reader(file)

#     for row in csv_reader:
#         list2.append(int(row[0]))


## NOTE PART 1

# sortedList1 = sorted(list1)
# sortedList2 = sorted(list2)
# sortedList1 = sorted(list1ex)
# sortedList2 = sorted(list2ex)
# difference = 0

# for x, y in zip(sortedList1, sortedList2): 
#     val = abs(x - y)
#     difference += val

# print(difference)

# # print(sortedList1)
# # print(sortedList2)
# # print(differencelist)



## NOTE PART 2

from collections import defaultdict

sortedList1ex = sorted(list1ex)
sortedList2ex = sorted(list2ex)
hashmap = {}

for x, y in zip(sortedList1ex, sortedList2ex): 
    if key in hashmap:
        hashmap[key].append(value)
    else:
        hashmap[key] = [value]


print(sortedList1ex)
print(sortedList2ex)
print(hashmap)


# sim_score = 0

# for x, y in zip(sortedList1, sortedList2):

#     val = abs(x - y)
#     sim_score += val

# print(difference)