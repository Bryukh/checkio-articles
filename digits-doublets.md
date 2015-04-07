# Digit Doublets

Do you know - we have the special island in CheckiO that is devoted by Lewis Carroll?
Charles Dodgson (aka Lewis Carroll) was an English writer, mathematician, logician,
Anglican deacon and photographer. And he wrote several books with mathemical and logical puzzles.
["Alice in Wonderland" island](http://www.checkio.org/station/alice/) contains
6 mission which are based on Lewis Carroll puzzles or some ideas from that cult book.
And today I would like to look at ["Digit Doublets" mission](http://www.checkio.org/mission/digits-doublets/share/911c36cfc7e36e7394548adbca23eb49/)

## Description

Doublets, sometimes known as Word ladder, is a word game invented by Charles Dodgson
(aka Lewis Carroll). A doublets puzzle begins with two words.
To solve the puzzle one must find a chain of different words 
to link the two together such that the two adjacent words differ by one letter.

For Example: **FLOUR** ⇒ FLOOR ⇒ FLOOD ⇒ BLOOD ⇒ BROOD ⇒ BROAD ⇒ **BREAD**

But in CiO puzzle we are using the given set of numbers with the same length and you should
find a chain of different numbers to link the two together
such that the two adjacent numbers differ by one digit.

# Solution

This mission maybe is looked hard or combinatorial, but let's little think about representation.
For example we are given this set of numbers: 
`111, 115, 175, 511, 515, 519, 591, 599, 875, 919, 999` and you need to link 111 and 999.
 
As we can see 111 can be changed at 115 and 511. From 511 we can move to 519 or 591. 
Stop. Is it look like a something familiar? Yes, this is a graph.

![Digit Graph](http://checkio.s3.amazonaws.com/blog/share/digit-graph.svg)

So we need to convert it to graph representation and find a path. 
I will not write a part about pathfinding, because you can easily find it in the recent article
-- ["Open Labyrinth" review](http://www.checkio.org/blog/find-path/).

```
from collections import defaultdict

def numbers2graph(numbers):
    graph = defaultdict(list)
    for i, n1 in enumerate(numbers):
        for n2 in numbers[i + 1:]:
            n1, n2 = str(n1), str(n2)
            if sum(d != n2[j] for j, d in enumerate(n1)) == 1:
                graph[n1].append(n2)
                graph[n2].append(n1)
    return graph
```

Next you are using an algorithm to find the shortest path through that graph and you got a solution.
 
# "Clear" CiO solutions

And [@PositronicLama](http://www.checkio.org/user/PositronicLlama/) wrote [a nice solution][PositronicLlama-solution]
 with A\* search. I recommend to read how is heuristics made. And interesting way to create a graph.
 
```
for a, b in itertools.combinations(numbers, 2):
    if digit_delta(a, b) == 1:
```

And [@LexCavalera's](http://www.checkio.org/user/LexCavalera) ["BFS" solution][LexCavalera-solution] is
created with OOP style and reading like a novel.

```
while to_search:
    current_number = to_search.pop(0)
```

# "Creative" CiO solutions

Honestly for "Creative" category I see only one solution by [@Juge_Ti](http://www.checkio.org/user/Juge_Ti/)
and this is ["Recursive"][Juge_Ti-recursive] code.

```
def f(l,c,u):
 if l[-1]in c:return c
 s=[f(l,c+[x],u|{x})for x in set(l)-u if sum(`c[-1]`[i]==`x`[i]for i in(0,1,2))==2]
 return min(s,key=len)if s else[1]*99
checkio=lambda l:f(l,[l[0]],{l[0]})
```

That's all folks. Bye for a next review.

_Valentin Bryukhanov aka Bryukh_

[PositronicLlama-solution]: http://www.checkio.org/mission/digits-doublets/publications/PositronicLlama/python-3/a/share/0a94d5a3b22839f0e88e53a7b548163f/
[LexCavalera-solution]: http://www.checkio.org/mission/digits-doublets/publications/LexCavalera/python-27/first/share/620074f0660cae9881b2e999651e5102/

[Juge_Ti-recursive]: http://www.checkio.org/mission/digits-doublets/publications/Juge_Ti/python-27/recursive/share/fb04f3e9d88479c9454386a37178ef14/