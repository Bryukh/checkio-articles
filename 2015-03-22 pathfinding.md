Hi, CiO friends!

Let's find a route between two points in the maze. 
For this we will look at ["Open Labyrinth"][open-labyrinth] mission.
In this mission you are given a map of a maze and you should find a path from one corner to other.
The maze can be represented as a graph where empty cells are nodes and adjacent cells are connected.
Because we don't need find the shortest path, so we can use various graph traversal algorithms.
We can look at that algorithms with our player solutions. 

> "So, the Labyrinth is a piece of cake, is it? Well, let's see how you deal with this little slice..."
 
## Breadth(Depth)-First Search

[Breadth-first_search](http://en.wikipedia.org/wiki/Graph_traversal#Breadth-first_search)
and [Depth-first_search](http://en.wikipedia.org/wiki/Graph_traversal#Depth-first_search)
are similar to each other.
DFS visits the child nodes before visiting the sibling nodes;
that is, it traverses the depth of any particular path before exploring its breadth.
BFS visits the parent nodes before visiting the child nodes.
A stack is used for DFS and a queue for BFS. So you can easily "switch" DFS to BFS.

[@spoty's][spoty] solution ["BFS + deque"][bfs-spoty] is a classical BFS realisation.
There is using the double ended queue. It's faster than list using and also we can
easily switch BFS to DFS just replace "q.popleft()" => "q.popright()".

```
from collections import deque
​
​
def checkio(maze_map, start=(1, 1), goal=(10, 10)):
    def get_adjacent(n):
        x, y = n
        n = [(x - 1, y, "N"), (x, y - 1, "W"),
             (x + 1, y, "S"), (x, y + 1, "E")]
        return [((x, y), c) for x, y, c in n if maze_map[x][y] != 1]
​
    q, v = deque([(start, "")]), set()
​
    while q:
        cords, path = q.popleft()
        if cords == goal:
            return path + mark
        if cords in v:
            continue
        v.add(cords)
        for pos, mark in get_adjacent(cords):
            if pos in v:
                continue
            else:
                q.append((pos, path + mark))
```

> Sarah: "You don't by any chance know the way through this labyrinth, do you?"

> The Worm: "Who, me? No, I'm just a worm. Say, come inside, and meet the missus"

## A\* search algorithm

As A* traverses the graph, it follows a path of the lowest expected total cost or distance,
keeping a sorted priority queue of alternate path segments along the way.
You can read more at [Wikipedia](http://en.wikipedia.org/wiki/A*_search_algorithm).

For priority queue Python has _heapq_ module and [@PositronicLlama's][PositronicLlama] solution
["First"][first-PositronicLlama] uses it and _namedtuples_ add readabilty here.

```
"""
Navigate a maze and return a route from the start to the finish.
Use A* to find a path in an efficient manner.
"""
import heapq
import collections
​
# The cardinal directions
DIRECTIONS = [
        (0, -1, 'N'),
        (0, 1, 'S'),
        (-1, 0, 'W'),
        (1, 0, 'E'),
    ]
​
Node = collections.namedtuple('Node', ['hist', 'ix', 'dist', 'pt', 'prev', 'direction'])
​
def heuristic(point, goal):
    """
    Return an admissible heuristic for the distance from point to goal.
    For the case of a grid with orthogonal movement, use the Manhattan distance.
    """
    return abs(point[0] - goal[0]) + abs(point[1] - goal[1])
​
def checkio(labyrinth):
    """
    Return a string of the characters [NSEW] describing a path through labyrinth.
    labyrinth: A list of lists.  '0' indicates a passable cell.
    """
    height, width = len(labyrinth), len(labyrinth[0])
    start = (1, 1)
    goal = (height - 2, width - 2)
    
    # Each node consists of (estimated path distance, ix, dist, (x, y), previous node, direction)
    # The ix field is a serial number to ensure that subsequent fields are
    # not compared.
    open = [Node(heuristic(start, goal), 0, 0, start, None, None)]
    
    # A set of all visited coordinates.
    explored = set()
    
    ix = 1
    while open:
        node = heapq.heappop(open)
        _, _, dist, point, prev, prev_d = node
        if point in explored:
            continue
        if point == goal:
            break
        explored.add(point)
        
        # Now consider moves in each direction.
        for dx, dy, d in DIRECTIONS:
            new_point = point[0] + dx, point[1] + dy
            if new_point not in explored and \
            not labyrinth[new_point[1]][new_point[0]]:
                h = dist + 1 + heuristic(new_point, goal)
                tie_break = 4 if prev_d != d else 0 # Prefer moving straight
                new_node = Node(h, ix + tie_break, dist + 1, new_point, node, d)
                heapq.heappush(open, new_node)
                ix = ix + 1
​
    # Return a path to node
    result = ''
    while node.prev is not None:
        result = node.direction + result
        node = node.prev
    return result
```

And look at ["Re-useable code'][macfreek-re-useable-code] by [@macfreek][macfreek].

> Sarah: That's not fair!

> Jareth: You say that so often, I wonder what your basis for comparison is?

## Dijkstra, Lee and others

BFS and A* are the most used algorithms, but there are many others.

[Dijkstra's algorithm](http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) is famous, so 
[@Miaou's][Miaou] ["Dijkstra's Forever !"][Miaou-dijkstras-forever] with explicit comments
can help to learn this algorithm.

[Lee algorithm](http://en.wikipedia.org/wiki/Lee_algorithm) is a BFS variation and 
[@suic][suic] demonstrates us how it's work in his ["First"][suic-first] solution.

Or you can turn always right (or left) to find the exit how it did
[@tetedemerou][tetedemerou] in ["Always a pit on the right"][tetedemerou-always-a-pit-on-the-right]
solution.

Random algorithm is an algorithm too and [@AndriusMk][AndriusMk] made
["Trolling :)"][AndriusMk-trolling] solution for this.

> Tell me Sarah, what do you think of my labyrinth?










<!---------------------------------->

[open-labyrinth]: http://www.checkio.org/mission/open-labyrinth/share/574bd1ded68c9705c5d6f07c6206be12/


[spoty]: http://www.checkio.org/user/spoty/
[PositronicLlama]: http://www.checkio.org/user/PositronicLlama/
[macfreek]: http://www.checkio.org/user/macfreek/
[Miaou]: http://www.checkio.org/user/Miaou/
[tetedemerou]: http://www.checkio.org/user/tetedemerou/
[suic]: http://www.checkio.org/user/suic/
[AndriusMk]: http://www.checkio.org/user/AndriusMk/


[bfs-spoty]: http://www.checkio.org/mission/open-labyrinth/publications/spoty/python-3/bfs-deque/share/df7f7cbb8228331c2346f853b79213c1/
[first-PositronicLlama]: http://www.checkio.org/mission/open-labyrinth/publications/PositronicLlama/python-3/first/share/dbdb1ff0ed90f3263a4b5fe98c6a282e/
[macfreek-re-useable-code]: http://www.checkio.org/mission/open-labyrinth/publications/macfreek/python-3/re-useable-code/share/3e8556d514ca04502facb316b41ff49d/
[tetedemerou-always-a-pit-on-the-right]: http://www.checkio.org/mission/open-labyrinth/publications/tetedemerou/python-3/always-a-pit-on-the-right/share/6f64e86a6bb7339c2782189f87d7ffa6/
[Miaou-dijkstras-forever]: http://www.checkio.org/mission/open-labyrinth/publications/Miaou/python-3/dijkstras-forever/share/abaade79d059202db1ded8fa4f9c02a4/
[suic-first]: http://www.checkio.org/mission/open-labyrinth/publications/suic/python-3/first/share/fe73ad8b279d7e7d250bccf2ddd8d60e/
[AndriusMk-trolling]: http://www.checkio.org/mission/open-labyrinth/publications/AndriusMk/python-27/trolling/share/c4a145933e55940992a5e0432258a1c0/