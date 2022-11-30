"""Info about sets."""

set_1 = {1, 2}
set_2 = {3, 4, 1}
extended_set = set_1 | set_2  # we extended 2 sets and got new set
print(extended_set)
intersection_set = set_1 & set_2  # we got intersection of 2 sets
print(intersection_set)
difference_set = set_1 - set_2  # we got difference of 2 sets
# (elements which have in set_1, but not in set_2)
print(difference_set)
symmetric_difference = set_1 ^ set_2  # we got elements which have on set_1 and set_2
# but not have in set_1 and set_2 together
print(symmetric_difference)
set_1.add(1)
print(set_1)
set_1.update([24, 23, 22])  # it works like extend but I changed this set
print(set_1)
set_1.remove(1)
print(set_1)
