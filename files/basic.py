from text import getText

## if you use "w" if gonna overwrite everything that you have in the file
# f = open('names.txt', 'w')

## if you use "a" if gonna append to everything that you have in the file
f = open('names.txt', 'a')
f.write('machine learning')
f.write('\n')
f.write('learning with the best')
f.write(getText())
f.close()
