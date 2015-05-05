Привет!

В этом обзоре я хочу рассмотреть классическую задачу известную под названием "Золотая гора".
И на CheckiO мы реализовали ее в задаче ["Золотая Пирамида"("Golden Pyramid")][golden-pyramid].

Представьте себе треугольник составленный из чисел. Одно число расположено в вершине.
Ниже размещено два числа, затем три и так до нижней грани.
Вы начинаете на вершине и нужно спустится к основанию треугольника.
На каждый ход вы можете спуститься на один уровень и выбрать между двумя числами под текущей позицией.
По ходу движения вы "собираете" и суммируете числа, которые проходите.
Ваша цель найти максимальную сумму, которую можно получить из различных маршрутов.

![GP Example](http://checkio.s3.amazonaws.com/blog/share/golden-pyramid-example.svg)

# Рекурсия

Первым делом в голову приходит мысль использовать рекурсию и просчитать все пути от вершины.
Когда мы спускаемся на один уровень, то все доступные числа ниже образуют новый меньший треугольник
и можно запустить нашу функцию уже для нового подмножества и так пока не достигнем основания.

```
def golden_pyramid(triangle, row=0, column=0, total=0):
    global count
    count += 1
    if row == len(triangle) - 1:
        return total + triangle[row][column]
    return max(golden_pyramid(triangle, row + 1, column, total + triangle[row][column]),
               golden_pyramid(triangle, row + 1, column + 1, total + triangle[row][column]))
```

Как мы видим на первом уровне мы запустим нашу функцию два раза, затем 4, 8, 16 раз и так далее.
В итоге результат мы получим сложность алгоритма 2<sup>N</sup>
и например для 100 уровневой пирамиды нам нужно будет уже где-то
≈ 10<sup>30</sup> вызовов функции. Многовато.

![GP Recursion](http://checkio.s3.amazonaws.com/blog/share/golden-pyramid-recursive.svg)


# Динамическое программирование

Что если попробовать использовать принцип динамического программирования и разбить нашу проблему
на множество мелких подзадач, результаты которых затем мы аккумулируем.
Попробуйте взлянуть на треугольник верх ногами. А теперь на второй уровень (то есть предпоследний от основания).
Для каждой ячейки мы можем решить, какой будет лучший выбор в наших маленьких трёхэлементных треугольничках. Выбираем лучший, суммируем с рассматриваемой ячейкой и записываем результат.
Таким образом мы получили наш треугольник, но на один уровень ниже. Повторяем данную операцию снова и
снова. В результате нам нужно (N-1)+(N-2)+...2+1 операций и сложность алгоритма равна N\*\*2.

```
def golden_pyramid_d(triangle):
    tr = [row[:] for row in triangle]  # copy
    for i in range(len(tr) - 2, -1, -1):
        for j in range(i + 1):
            tr[i][j] += max(tr[i + 1][j], tr[i + 1][j + 1])
    return tr[0][0]
```

![GP Dynamic](http://checkio.s3.amazonaws.com/blog/share/golden-pyramid-dynamic.svg)

# Решение игроков CheckiO

[@gyahun_dash] написал интересную реализацию описанного выше метода ДП в своем
["DP" решении][gyahun_dash-dp]. Он использовал "reduce", чтобы проходить по парам строкам и
"map" чтобы обработать каждую из них.

```
from functools import reduce
​
def sum_triangle(top, left, right):
    return top + max(left, right)
​
def integrate(lowerline, upperline):
    return list(map(sum_triangle, upperline, lowerline, lowerline[1:]))
​
def count_gold(pyramid):
    return reduce(integrate, reversed(pyramid)).pop()
```

[@evoynov][evoynov]  использовал двоичные числа, чтобы перебрать все возможные маршруты, представленные как последовательность 1 и 0
 в своем  ["Binaries" решении][evoynov-binaries].
 И это наглядный пример сложности алгоритма с рекурсией и перебором всех маршрутов.

```
def count_gold(p):
    path = 1 << len(p)
    res = 0
    while bin(path).count("1") != len(p) + 1:
        s = ind = 0
        for row in range(len(p)):
            ind += 1 if row > 0 and bin(path)[3:][row] == "1" else 0
            s += p[row][ind]
        res = max(res, s)
        path += 1
    return res
```

И чтобы не было скучно посмотрим на легкий мозгодробитель от
[@nickie's][nickie] и его ["Functional DP" однострочник][nickie-functional],
который только формально состоит из двух строк.
Конечно это решение из категории "Творческих" ("Creative").
Не думаю, что автор использует такое на боевом коде. А просто для так для веселья, почему бы и нет.
```
count_gold=lambda p:__import__("functools").reduce(lambda D,r:[x+max(D[j],D[j+1])
for j,x in enumerate(r)],p[-2::-1],list(p[-1]))[0]
```

Вот и все на сегодня. Делитесь вашими идеями и мыслями.

_Валентин Брюханов aka Bryukh_



<!--------------------------------------------------------------------------------------------------------------------->

[golden-pyramid]: http://www.checkio.org/mission/golden-pyramid/share/b88523a147fdb0960da155eb777729f0/

[gyahun_dash]: http://www.checkio.org/user/gyahun_dash/
[evoynov]: http://www.checkio.org/user/evoynov/
[evoynov]: http://www.checkio.org/user/evoynov/

[gyahun_dash-dp]: http://www.checkio.org/mission/golden-pyramid/publications/gyahun_dash/python-3/dp/share/28008da26f7ecba0593f7b71a5250b25/
[evoynov-binaries]: http://www.checkio.org/mission/golden-pyramid/publications/evoynov/python-3/binaries/share/95c5578eef9be0c793fc37fe54bdc95e/
[nickie-functional]: http://www.checkio.org/mission/golden-pyramid/publications/nickie/python-3/functional-dp/share/98bff2a8ad1f0ca4897de6e884ec384d/
