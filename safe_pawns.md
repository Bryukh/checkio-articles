Hi, Che..hm..ss lovers.

Today we will take a look at one of CheckiO's Chess missions ["Safe Pawns"](http://www.checkio.org/mission/pawn-brotherhood/share/53e5148cf5d6992948bab44eaded07cc/).
I hope you've heard about the ancient game [Chess](http://en.wikipedia.org/wiki/Chess) by now.
In this mission we will take a closer look at the weakest but most numerous
(and maybe even dangerous) chess piece: **pawns**.

A pawn is generally a weak unit, but we have 8 of them (sometimes less) which we can use to build a pawn defense wall.
With this strategy, one pawn defends the other pieces.
A pawn is safe if another pawn can capture a unit on that square.
We have several white pawns on the chess board, and we only control the white pawns.
You should design your code to find how many pawns are safe in the given scenario.

So our goal is to count safe pawns. For this we can check each of them for a defending neighbor. 
Each cell can have no more than two possible defending cells. 
The both of them are placed one line below, one in the left and one in the right column.

So `pawn` is the cell coordinates for the checked pawn and rank is `p[1]`. To find the
rank use `str(int(p[1]) - 1)` or `chr(ord(p[1]) - 1)`. To find left and right files we can use the
same method: `chr(ord(p[0]) - 1)` and `chr(ord(p[0]) + 1)`. Yes, I know that for
`a1` we will get "\`0" and "b0", but this is not a problem for our solution because we have a set
of correct pawn coordinates. So if we use the "wrong" coordinates, then we won't find them.

Now gather it into a function and, voilà, we have a solution:

```
def safe_pawns(pawns):
    safe_count = 0
    for p in pawns:
        if (chr(ord(p[0]) - 1) + chr(ord(p[1]) - 1) in pawns or
                chr(ord(p[0]) + 1) + chr(ord(p[1]) - 1) in pawns):
            safe_count += 1
    return safe_count
```

After taking a look, almost all CiO player solutions are kinda same lookinh, so today I'll show you a neat one one-liner by
[@Juge_Ti](http://www.checkio.org/user/Juge_Ti/) ([link](http://www.checkio.org/mission/pawn-brotherhood/publications/Juge_Ti/python-27/shorter-than-vekys/share/ebe84cb200b9da18ec4f8f18ec7c6e58/))

```
safe_pawns=lambda s:sum(bool({chr(ord(x)+k)+str(int(y)-1)for k in(-1,1)}&s)for x,y in s)
```

That's all folks. Do you want me to review another specific mission? Then let me know in comment section below!
