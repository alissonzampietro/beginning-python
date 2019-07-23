import os

## Below you have two ways of iterate
with open('./datasets/iris.data', 'r') as f:
    for linha in f.readlines():
        print(linha)

# with open('./datasets/iris.data', 'r') as f:
#     print(f.read())

# with open('./datasets/iris.data', 'r') as f:
#     list = f.read().splitlines()
#     print(len(list))
#     print(list[1])