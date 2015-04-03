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


g = numbers2graph([111, 115, 175, 511, 515, 519, 591, 599, 875, 919, 999])

for k in sorted(g):
    print(k, g[k])