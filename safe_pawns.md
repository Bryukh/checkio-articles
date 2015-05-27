Hi, Che..hm..ss lover.

Today we will look at one of CheckiO Chess mission ["Safe Pawns"](http://www.checkio.org/mission/pawn-brotherhood/share/53e5148cf5d6992948bab44eaded07cc/).
I hope you about the ancient game [Chess](http://en.wikipedia.org/wiki/Chess).
And in this mission we will look at the weakest but numerous
(and maybe dangerous) chess pieces - **pawns**.

A pawn is generally a weak unit, but we have 8 of them (or less)
which we can use to build a pawn defense wall.
With this strategy, one pawn defends the others.
A pawn is safe if another pawn can capture a unit on that square.
 We have several white pawns on the chess board and only white pawns.
  You should design your code to find how many pawns are safe.

So our goal is count safe pawns. For this we can check each of them and look is it have a defender
neighbour or not. Each cell can have no more than two possible defender cell. The both of them
are placed one line below, one in left and one in right column from the checked.

Let's `pawn` is a cell coordinates for the checked pawn, then rank is `p[1]` and to find below
rank -- `str(int(p[1]) - 1)` or `chr(ord(p[1]) - 1)`. To find left and right files we can use the
same (second) method -- `chr(ord(p[0]) - 1)` and `chr(ord(p[0]) + 1)`. Yes, I know that for
`a1` we will get "\`0" and "b0". But this is not a problem for our solution, because we have a set
of correct pawn coordinates. So if we use "wrong" coordinates, then we don't find them.

Now gather it a function and we have a solution:

```
def safe_pawns(pawns):
    safe_count = 0
    for p in pawns:
        if (chr(ord(p[0]) - 1) + chr(ord(p[1]) - 1) in pawns or
                chr(ord(p[0]) + 1) + chr(ord(p[1]) - 1) in pawns):
            safe_count += 1
    return safe_count
```

Almost all CiO player solutions are too like each other, so today I put only one one-liner by
[@Juge_Ti](http://www.checkio.org/user/Juge_Ti/) ([link](http://www.checkio.org/mission/pawn-brotherhood/publications/Juge_Ti/python-27/shorter-than-vekys/share/ebe84cb200b9da18ec4f8f18ec7c6e58/))

```
safe_pawns=lambda s:sum(bool({chr(ord(x)+k)+str(int(y)-1)for k in(-1,1)}&s)for x,y in s)
```

That's all (one) folk. Maybe you want to ask about some mission review, then write me in comments.
