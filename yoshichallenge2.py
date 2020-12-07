# a = [3, 6, 9, 10, 5, 3, 2, 1, 11]
# curhi = 0
# for x in a:
#     if curhi<x and x%2==0:
#         curhi = x
#
# print(curhi)
#
#
#


def even_number(whatever):
    return whatever % 2 == 0

a = [3, 6, 9, 10, 5, 3, 2, 1, 11]

filteredN = filter(even_number, a)
print(max(filteredN));
