## Below you have two ways of iterate
with open('datasets/iris.data', 'r') as f:
    for linha in f.readlines():
        print(linha)

with open('datasets/iris.data', 'r') as f:
    print(f.read())