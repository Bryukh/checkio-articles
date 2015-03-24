Hi!

Let's look at a classical CS problem that was realised as the Checkio mission.
I mean ["Golden Pyramid"][golden-pyramid] mission.

Consider a triangle of numbers. There is one number in the top of the triangle.
On the next level - two numbers, then three and so on.
You are start at the top and should down to the bottom of the triangle.
For each step down you can move to on of two cell below current.
And you "collect" (summarize) passed numbers.
Your goal is find the maximum possible sum of numbers for all possible routes from top to bottom.

![GP Example](http://checkio.s3.amazonaws.com/blog/share/golden-pyramid-example.svg)

# Recursive

The first obvious idea is to use recursion and calculate all paths from top to down.
When we down to one level, then all below available cells are the new sub-triangle and
we can start our function one more time for the new triangle. And so on until we reach the bottom.
Simple and obviously.

```
def golden_pyramid(triangle, row=0, column=0, total=0):
    global count
    count += 1
    if row == len(triangle) - 1:
        return total + triangle[row][column]
    return max(golden_pyramid(triangle, row + 1, column, total + triangle[row][column]),
               golden_pyramid(triangle, row + 1, column + 1, total + triangle[row][column]))
```

But as we can see for the first level we run our function 2 times, then 4, 8, 16....
So as result we will get 2<sup>N</sup> complexity and 
for the hundred-storied pyramid we need ≈ 10<sup>30</sup> function calls. Hm... 

![GP Recursion](http://checkio.s3.amazonaws.com/blog/share/golden-pyramid-recursive.svg)


# Dynamic Programming

But what if we will use dynamic programming method and break our problem to small pieces,
which can be merged then.
For simplicity look at the triangle upside down. Now look at the second (from new top) level.
For each cell we can choose what is the best possible for this small three element triangle.
Choose the best from the first level (early bottom), summarize with current cell value and write it.
Now we have the new shorter triangle and can repeat this operation again and again.
As result we have (N-1)+(N-2)+...2+1 operations and this is N\*\*2 complexity.

```
def golden_pyramid_d(triangle):
    tr = [row[:] for row in triangle]  # copy
    for i in range(len(tr) - 2, -1, -1):
        for j in range(i + 1):
            tr[i][j] += max(tr[i + 1][j], tr[i + 1][j + 1])
    return tr[0][0]
```

![GP Dynamic](http://checkio.s3.amazonaws.com/blog/share/golden-pyramid-dynamic.svg)

# Checkio Player Solutions

[@gyahun_dash] made the interesting realisation of dynamic programming method in 
["DP" solution][gyahun_dash-dp]. He used "reduce" to work at rows by pairs with accumulating and
"map" to process each level.
 
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

[@evoynov][evoynov] used binary numbers to define all possible paths as combinations of 1 and 0
 in ["Binaries" solution][evoynov-binaries]. 
 But this solution has the complexity as recursive method that was described early. 

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

And just for final little brain breaking puzzle (don't worry it's not too hard) with
[@nickie's][nickie] in ["Functional DP" one-liner][nickie-functional] which is only formally 
two-liners. Of course this is solution from "Creative" category and don't think that @nickie
writes this for production. Just for fun.

```
count_gold=lambda p:__import__("functools").reduce(lambda D,r:[x+max(D[j],D[j+1])
for j,x in enumerate(r)],p[-2::-1],list(p[-1]))[0]
```

That's all folks. Propose your ideas for the next articles.

_Valentin Bryukhanov aka Bryukh_



<!--------------------------------------------------------------------------------------------------------------------->

[golden-pyramid]: http://www.checkio.org/mission/golden-pyramid/share/b88523a147fdb0960da155eb777729f0/

[gyahun_dash]: http://www.checkio.org/user/gyahun_dash/
[evoynov]: http://www.checkio.org/user/evoynov/
[evoynov]: http://www.checkio.org/user/evoynov/

[gyahun_dash-dp]: http://www.checkio.org/mission/golden-pyramid/publications/gyahun_dash/python-3/dp/share/28008da26f7ecba0593f7b71a5250b25/
[evoynov-binaries]: http://www.checkio.org/mission/golden-pyramid/publications/evoynov/python-3/binaries/share/95c5578eef9be0c793fc37fe54bdc95e/
[nickie-functional]: http://www.checkio.org/mission/golden-pyramid/publications/nickie/python-3/functional-dp/share/98bff2a8ad1f0ca4897de6e884ec384d/