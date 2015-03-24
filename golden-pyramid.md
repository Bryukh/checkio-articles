Hi!

Let's look at a classical CS problem that was realised as Checkio mission.
I tell about ["Golden Pyramid"][golden-pyramid].

Consider a triangle of numbers. There is one number in the top of the triangle.
On the next level - two numbers, then three and so on.
You are start at the top and should down to the bottom of the triangle.
For each step down to the next level you can move to on of two cell below current.
And for each step you "collect" (summarize) passed numbers.
Your goal is find the maximum possible sum of numbers for all possible routes from top to bottom.

![GP Example](http://checkio.s3.amazonaws.com/blog/share/golden-pyramid-example.svg)

# Recursive

The first obvious idea is to use recursive and check various path from top to down.
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

But as we can see for first level we run our function 2 times, then 4, 8, 16....
So as result we will get 2\*\*N complexity. Not good.

![GP Recursion](http://checkio.s3.amazonaws.com/blog/share/golden-pyramid-recursive.svg)


# Dynamic Programming

But what if we will use dynamic programming method and break our problem to small pieces, which can
be accumulated.
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















[golden-pyramid]: http://www.checkio.org/mission/golden-pyramid/share/b88523a147fdb0960da155eb777729f0/

[golden-pyramid-example_svg]: http://checkio.s3.amazonaws.com/blog/share/golden-pyramid-example.svg