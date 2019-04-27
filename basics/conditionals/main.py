import random

number = random.randint(1,200)


if 0 <= number <= 50:
    print(str(number)+' is low')
elif 51 <= number <= 120:
    print(str(number)+' is medium')
elif 121 <= number < 201:
    print(str(number)+' is high')
