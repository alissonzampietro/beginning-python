## Importing class
import person
from person import Person

# weird hahahha
p = person.Person('Alisson', 24)
print(p.name)
print(p.age)

# normal hahahha
p1 = Person('Alisson', 24)
print(p1.name)
print(p1.age)
p.showName()