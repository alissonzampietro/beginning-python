# SETS
# Doesn't contain repeated elements

a = [1,2,3,4]
# you can convert an array in sets
b = set(a)
print('array to sets: '+str(b))

s = set()
#never repeat elements
s.add(10)
s.add(10)
s.add(20)
s.add(30)

# Show sets
print(s)

s1 = {1,2,3,4}
s2 = {4,5,6}

union = s1.union(s2)
intersection = s1.intersection(s2)
difference = s1.difference(s2)

print('union: '+str(union))
print('intersection: '+str(intersection))
print('difference: '+str(difference))

#  Sets doesn't support indexing, so you can't do that:
# print(s1[1])


# See all methods that set has
# print(help(set))