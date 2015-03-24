from timeit import timeit
import random

from itertools import combinations

def break_rings(rings):
    """Compute the number of broken rings be substracting the ones we have
       left from the ones we started with"""
    individuals = set()
    for r in rings:
        individuals.update(r)
    return len(individuals) - keep_rings((individuals, rings))

def keep_rings(i_and_r):
    """ Returns the number of surviving rings """
    # Treating this as an exhaustive search problem.
    #
    # Consider the first ring sets; see what happens if breaks either
    # of the two rings and take the better result.
    #
    # Normal by removing discarding the ring sets where at least one
    # ring has been broken.
    #
    # Then recur.
    #
    individuals, rings = i_and_r
    if not rings:
        return len(individuals)
    return max(keep_rings(break_loop(True,i_and_r)),
               keep_rings(break_loop(False,i_and_r)))

def break_loop(lower,i_and_r):
    """ Constructs a new set of individiuals and or rings based on breaking
        one of the two ring first in the first set"""
    # lower says whether to break the lower number of the two rings
    # in the frist set
    individuals, rings = i_and_r
    if not rings:
        return len(individuals)
    the_broken = None
    if lower:
        the_broken = min(rings[0])
    else:
        the_broken = max(rings[0])
    individuals = individuals - {the_broken}
    rings = rings_broken(rings, the_broken)
    return (individuals, rings)

def rings_broken(rings, the_broken):
    return [ring for ring in rings if the_broken not in ring]





def break_rings_sim(rings):
    uniq_rings = set.union(*rings)
    for n in range(1, len(uniq_rings)):
        for destroy in combinations(uniq_rings, n): # we break n rings
            if all(ring & set(destroy) for ring in rings): return n # found

def generate_test(N=9):
    numbers = list(range(1, N + 1))
    n_connections = random.randint(1, N * 3)
    connection = []
    for dummy in range(n_connections):
        var = set(random.choice(list(combinations(numbers, 2))))
        if var not in connection:
            connection.append(var)
    return connection

break_rings_veky = lambda rings: min(len(set.union(*bits)) for bits in __import__
    ("itertools").product(*([link - {w} for w in link] for link in rings)))

break_rings_diz=lambda r:min(len(set(c))for c in __import__("itertools").product(*r))

T = generate_test(15)

print(T)
print("sim")
print(timeit("break_rings_sim(T)", "from __main__ import break_rings_sim, T", number=10))
print("radul")
print(timeit("break_rings(T)", "from __main__ import break_rings, T", number=10))
# print("veky")
# print(timeit("break_rings_veky(T)", "from __main__ import break_rings_veky, T", number=10))
print("diz")
print(timeit("break_rings_diz(T)", "from __main__ import break_rings_diz, T", number=10))