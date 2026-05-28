import random
import heapq
from itertools import combinations
from collections import defaultdict

VERTICES = ['s', 'A', 'B', 't']
SOURCE = 's'

def GraphoDimiourgosOTyxaios(vertices=VERTICES, p=0.7, q=0.3):

    edges = {}
    for u, v in combinations(vertices, 2):
        if random.random() < p:
            if random.random() < q:
                edges[(u, v)] = -1
                edges[(v, u)] = +1
            else:
                edges[(u, v)] = +1
                edges[(v, u)] = -1
    return edges

def Geitniash(vertices, edges):
    adj = {v: [] for v in vertices}
    for (u, v), w in edges.items():
        adj[u].append((v, w))
    return adj

def dijkstra(vertices, edges, source):

    adj = Geitniash(vertices, edges)
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0
    pq = [(0, source)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v, w in adj[u]:
            if v not in visited and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist


def bellman_ford(vertices, edges, source):

    dist = {v: float('inf') for v in vertices}
    dist[source] = 0
    n = len(vertices)
    edge_list = list(edges.items())

    for _ in range(n - 1):
        updated = False
        for (u, v), w in edge_list:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    ArnhtikosKyklos = False
    for (u, v), w in edge_list:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            ArnhtikosKyklos = True
            break

    return dist, ArnhtikosKyklos

def ArnhtikesAkres(edges):
    return any(w < 0 for w in edges.values())


def dists_equal(d1, d2, vertices):
    return all(d1[v] == d2[v] for v in vertices)

SPECIFIC_EDGES = {
    ('s', 'A'): +1, ('A', 's'): -1,
    ('s', 'B'): -1, ('B', 's'): +1,
    ('A', 'B'): +1, ('B', 'A'): -1,
    ('A', 't'): +1, ('t', 'A'): -1,
    ('B', 't'): +1, ('t', 'B'): -1,
}

def SygkekrimenoStigmiotypoTypeSheet():
    print("Apo Sygkekrimeno Stgmiotypo")

    print("\n Akmes kai Varh")
    for (u, v), w in sorted(SPECIFIC_EDGES.items()):
        print(f"  {u} -> {v}: {w:+d}")

    neg = [(u, v, w) for (u, v), w in SPECIFIC_EDGES.items() if w < 0]
    print(f"\nOi Arnhtikes akmes einai :({len(neg)}):")
    for u, v, w in neg:
        print(f"  {u} -> {v}: {w:+d}")

    bf, ArnhtikosKyklos = bellman_ford(VERTICES, SPECIFIC_EDGES, SOURCE)

    print(f"\nYparxei arnhtikos kyklos ? {'Nai yparxei' if ArnhtikosKyklos else 'Oxi Dystyxws'}")

    print("\n O Bellman-Ford gia s:")
    for v in VERTICES:
        val = bf[v] if bf[v] != float('inf') else '∞'
        print(f"  dist[{v}] = {val}")

    if ArnhtikosKyklos or ArnhtikesAkres(SPECIFIC_EDGES):
        return

    dijk = dijkstra(VERTICES, SPECIFIC_EDGES, SOURCE)

    print("\n O Dijkstra gia s:")
    for v in VERTICES:
        print(f"  dist[{v}] = {dijk[v]}")

    correct = dists_equal(dijk, bf, VERTICES)
    print(f"\nΔijkstra == Bellman-Ford: {'Nai einai!' if correct else 'Dystyxws oxi, tha mporouse alla telika den mporei'}")

def Prosomoioths(AritmosDokimwn=10_000, seed=43):
    random.seed(seed)

    total = AritmosDokimwn
    MetrhthsIOiArnhtikesAkmes     = 0
    MetrhthsIIOiArnhtikoiKykloi     = 0
    MetrhthsIIIOSwstos       = 0   
    MetrhthsIVOLathos     = 0   
    MetrhthsVOSwstosArnhtikos   = 0   
    MetrhthsVIOLathosArnhtikos = 0   

    for _ in range(total):
        edges = GraphoDimiourgosOTyxaios()

        neg_edges          = ArnhtikesAkres(edges)
        bf_dist, ArnhtikosKyklos = bellman_ford(VERTICES, edges, SOURCE)

        if neg_edges:
            MetrhthsIOiArnhtikesAkmes += 1
        if ArnhtikosKyklos:
            MetrhthsIIOiArnhtikoiKykloi += 1

        if not ArnhtikosKyklos:
            if not neg_edges:
                dijk_dist = dijkstra(VERTICES, edges, SOURCE)
                correct = dists_equal(dijk_dist, bf_dist, VERTICES)
                if correct:
                    MetrhthsIIIOSwstos += 1
                else:
                    MetrhthsIVOLathos += 1
            else:
                MetrhthsVIOLathosArnhtikos += 1

    no_cycle = total - MetrhthsIIOiArnhtikoiKykloi
    with_neg_no_cycle = MetrhthsVOSwstosArnhtikos + MetrhthsVIOLathosArnhtikos

    print(f"Trexw thn Prosomoiwsh me {total:,} tyxaious graphous kai parametrouw (p=0.7, q=0.3)")

    print(f"\nOi Graphoi me arnhtikes akmes einai : {MetrhthsIOiArnhtikesAkmes:6,}  "
          f"({100*MetrhthsIOiArnhtikesAkmes/total:.1f}%)")
    print(f"Oi Graphoi me arnhtiko kyklo einai  : {MetrhthsIIOiArnhtikoiKykloi:6,}  "
          f"({100*MetrhthsIIOiArnhtikoiKykloi/total:.1f}%)")

    print(f"\n Oi Graohoi xwris arnhtiko kyklo einai : {no_cycle:6,} kai gia aytous")
    if no_cycle:
        print(f"  O Dijkstra htan swstos         : {MetrhthsIIIOSwstos:6,} fores "
              f"({100*MetrhthsIIIOSwstos/no_cycle:.1f}%)")
        print(f"  O Dijkstra htan lathos    : {MetrhthsIVOLathos:6,}  fores"
              f"({100*MetrhthsIVOLathos/no_cycle:.1f}%)")

    print(f"\nGia tous graphous me arnhtikes akmes kai xwris arnhtiko kyklo pou einai : "
          f"{with_neg_no_cycle:,}")
    if with_neg_no_cycle:
        print(f"  O Dijkstra den etrexe (skipped)) : {MetrhthsVIOLathosArnhtikos:6,}  "
              f"({100*MetrhthsVIOLathosArnhtikos/with_neg_no_cycle:.1f}%)")


if __name__ == '__main__':
    SygkekrimenoStigmiotypoTypeSheet()
    Prosomoioths(10_000)