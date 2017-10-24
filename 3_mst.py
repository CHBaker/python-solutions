"""
	Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:

	{'A': [('B', 2)],
	 'B': [('A', 2), ('C', 5)], 
	 'C': [('B', 5)]}
	Vertices are represented as unique strings. The function definition should be question3(G)
"""
from operator import itemgetter


def cycle_exists(G):
    marked = {u: False for u in G}
    found_cycle = [False]
    for u in G:
        if not marked[u]:
            dfs_visit(G, u, found_cycle, u, marked)
        if found_cycle[0]:
            break
    return found_cycle[0]


def dfs_visit(G, u, found_cycle, pred_node, marked):
    if found_cycle[0]:
        return
    marked[u] = True
    for v in G[u]:
        if marked[v] and v != pred_node:
            found_cycle[0] = True
            return
        if not marked[v]:
            dfs_visit(G, v, found_cycle, u, marked)


def question3(adjDict):
    # this dict will be the final dict
    newDict = {key: list([]) for key in adjDict.keys()}
    # this dict will match newDict with a stripped down more
    # straight forward data structure, and used to test for cycles
    strippedDict = {key: list([]) for key in adjDict.keys()}
    # this list will be used for the main loop to make sure each loop
    # occurs only one time.
    edgeList = []
    seen = []

    for vert in adjDict:
        seen.append(vert)
        for edge in adjDict[vert]:
            if edge[0] not in seen:
                edge = list(edge)
                edge.insert(0, vert)
                edge = tuple(edge)
                edgeList.append(edge)

    list.sort(edgeList, key=itemgetter(2))

    for union in edgeList:
        newDict[union[0]].append((union[1], union[2]))
        newDict[union[1]].append((union[0], union[2]))
        strippedDict[union[0]].append(union[1])
        strippedDict[union[1]].append(union[0])
        if cycle_exists(strippedDict):
            newDict[union[0]].remove((union[1], union[2]))
            newDict[union[1]].remove((union[0], union[2]))
            strippedDict[union[0]].remove(union[1])
            strippedDict[union[1]].remove(union[0])
    return newDict


a = {
    'A': [('B', 3), ('D', 4)],
    'B': [('A', 3), ('E', 4), ('F', 6)],
    'C': [('E', 5)],
    'D': [('A', 4)],
    'E': [('B', 4), ('F', 5), ('C', 5)],
    'F': [('B', 6), ('E', 5)]
}

print question3(a)
# Should return
# {
#   'A': [('B', 3), ('D', 4)],
#	'B': [('A', 3), ('E', 4)],
#	'C': [('E', 5)],
#	'D': [('A', 4)],
#	'E': [('B', 4), ('C', 5), ('F', 5)],
#	'F': [('E', 5)]
# }




