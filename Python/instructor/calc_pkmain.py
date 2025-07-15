# case1

import pkcalc.calc as calc

print(calc.name)
print(calc.add(5,6))


# case 2

from pkcalc.calc import name, add

print(name)
print(add(5,6))


# case 3

from pkcalc import add, sub

result1 = add(3, 5)  # 8을 반환
result2 = sub(10, 4)  # 6을 반환

print(result1)  # 8 출력
print(result2)  # 6 출력
