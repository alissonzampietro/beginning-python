tupla = (1,[1,2],3)
# You can't reassign tuples after they had been assigned
# tupla[1] = 2

print('Tuples: '+str(tupla))

# But you can reassign nested array values from tuples
tupla[1][0] = 56
print('Nested array of the tuple reassigned: '+str(tupla))

# Get all methods from the tupla class
# print(help(tupla))

# Count ocurrences of determined value
print('Counts: '+str(tupla.count(1)))


print('Index: ' + str(tupla.index(3)))