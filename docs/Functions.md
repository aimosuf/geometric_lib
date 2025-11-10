### Функции для круга
## Area
```
def area(r):
    return math.pi * r * r
```
Принимает число r (радиус) и возвращает площадь круга. По формуле S = πR².
**Пример вызова:**
```
from circle import area
print(area(5))  # 78.53981633974483
```
## Perimeter
```
def perimeter(r):
    return 2 * math.pi * r
```
Принимает число r (радиус) и возвращает периметр круга. По фомуле P = 2πR.
**Пример вызова:**
```
from circle import perimeter
print(perimeter(5))  # 31.41592653589793
```

### Функции для квадрата
## Area
```
def area(a):
    return a * a
```
Принимает число a b возвращает площадь. По формуле S = a².
**Пример вызова:**
```
from square import area
print(area(4))  # 16
```
## Perimeter
```
def perimeter(a):
    return 4 * a
```
Принимает число a (сторону) и возвращает периметр. По формуле P = 4a.
**Пример вызова:**
```
from square import perimeter
print(perimeter(4))  # 16
```