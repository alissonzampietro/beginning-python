## in the examble below, you are importing the whole module with all methods
import calc_area

## in the example below you are importing just the methods that you want to use
from calc_area import square, circle

print(calc_area.square(3))
print(calc_area.circle(2))


print(square(2))