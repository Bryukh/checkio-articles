![Pigeons](http://checkio.s3.amazonaws.com/blog/share/hungry-pigeons.png)

Hi, CiO Friends!

On our landing page you can find a mission we've designed for newer CheckiO players: ["Feed Pigeons"][mission]. 
Sometimes this mission be a little challenging, so I thought we'd take a look at some different ways players have taken this mission on.

## Description

I feed one pigeon, a minute later two more fly by and a minute after that another 3.
Then 4, and so on (Ex: 1+2+3+4+...). 
One portion of the food lasts a pigeon for a minute, so the pigeons get to eat on a first come first serve basis. 
Pigeons are hungry animals and eat without knowing when to stop. 
If I have N portions of bird feed, how many pigeons will be fed with at least one portion of wheat?

## Simple

The simplest way to solve this problem is by using a step-by-step model and repeat all stages of feeding.
Create a minute counter and for each minute that goes by, we reduce the number of wheat portions and add new pigeons.
We should pay attention during this step, because the first pigeon to arrive gets to eat first, even if they've already eaten.
In our solution, a "minute" is the same as the quantity of newly arrived pigeons.

```
def checkio(portions):
    """Simple and straight"""
    fed = minute = pigeons = 0
    while portions >= 0:
        portions -= pigeons
        minute += 1
        if portions <= 0:
            return fed
        if minute < portions:
            fed += minute
            portions -= minute
        else:
            fed += portions
            return fed
        pigeons += minute
    return fed
```

## Sequence

If we write the solution results for several input values, then we can see that these numbers create a sequence.

`1, 1, 2, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10...`

If you see the pattern, you're on the right track. Now, we need to write a generator, and honestly
we can receive all answers from 1 to N in one run.

```
def checkio(portions):
    step, i, results = 1, 1, []
    while len(results) < portions + 1:
        results.extend([i] * (i + 1))
        results.extend(range(i + 1, i + 1 + step))
        step += 1
        i += step
    return results[portions]
```

## Math

This mission can be solved with pure mathematics. (well, almost pure) and O(1) complexity.
[@bunnychai](http://www.checkio.org/user/bunnychai/) has proved this with the
["Arithmetic" solution][arithmetic]

```
def checkio(number):
    k = int((6 * number) ** (1.0 / 3))
    if k * (k + 1) * (k + 2) > 6 * number:
        k -= 1
    t = k * (k + 1) / 2
    s = t * (k + 2) / 3
    return t + max(number - s - t, 0)
```

Here's an another variant by [@DiEvAl](http://www.checkio.org/user/DiEvAl/) with the ["First" solution][dieval].
In it, you can find an explanation for the the math.

```
def checkio(n):
    # After m minutes there are m(m+1)/2 birds and we've used m(m+1)(m+2)/6 portions of wheet.
    # Solving the equation x(x+1)(x+2)=6n (http://www.wolframalpha.com/input/?i=x%28x%2B1%29%28x%2B2%29%3D6n)
    # gives us only 1 positive real root for a > 0:
    # x = (sqrt(3) sqrt(243 a^2-1)+27 a)^(1/3)/3^(2/3)+1/(3^(1/3) (sqrt(3) sqrt(243 a^2-1)+27 a)^(1/3))-1
    t = ((9*n**2 - 1/27) ** (1/2) + 3*n) ** (1/3)
    x = t + 1/(3*t) - 1
    m = int(x)
    return max(m*(m+1)/2, n - m*(m+1)*(m+2)/6)
```

## Creative

And as usual, I've cherry-picked some "Creative" solutions for dessert.
For example, this [golf solution][golf] by [@melpon](http://www.checkio.org/user/melpon/)

```
f=lambda n,y=0,i=0:n<y and max(n,y-i+1)or f(n-y,sum(range(i+1)),i+1)
checkio=f
```

And [@veky](http://www.checkio.org/user/veky/) has this ["Optimal" solution][optimal], where the math is twisted with a binary search. You can find hints on how it works in the comments, or even just ask him if you want to know more.

```
def pbs(cond, start=0):
    """last int after start satisfying cond
    Precondition: cond(n)=>cond(n-1) & cond(start) & exists n>start not cond(n)
    Complexity: max. 2*ld(result-start), calls cond on distinct numbers only"""
    step = 1
    while cond(start + step): step <<= 1
    start += step >> 1
    step >>= 2
    while step:
        if cond(start + step): start += step
        step >>= 1
    return start
​
def checkio(n):
    k = pbs(lambda k: k**3 - k <= 6*n)
    return max(n - (k**3 - k)//6, (k**2 - k)//2)
```

That's all folks. Be careful feeding the Hungry Pigeons ;-)

_Valentin Bryukhanov aka Bryukh_

[mission]: http://www.checkio.org/mission/feed-pigeons/share/fabf278379f4a8217eef2549b2ac4164/
[arithmetic]: http://www.checkio.org/mission/feed-pigeons/publications/bunnychai/python-27/arithmetic/share/7f72e750ee5446ed97e7396976564c16/

[dieval]: http://www.checkio.org/mission/feed-pigeons/publications/DiEvAl/python-3/first/share/30897afff7da3f66244bb05523719eb0/
[golf]: http://www.checkio.org/mission/feed-pigeons/publications/melpon/python-3/first/share/92814969c22d9d20d829547c190f2007/
[optimal]: http://www.checkio.org/mission/feed-pigeons/publications/veky/python-3/optimal/share/716ba8c58f595d8317a40f55642a572c/
