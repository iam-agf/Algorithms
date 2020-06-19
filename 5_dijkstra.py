from collections import defaultdict
from math import inf

graph = {

'a':{'b':3,'c':4, 'd':7},
'b':{'c':1,'f':5},
'c':{'f':6,'d':2},
'd':{'e':3, 'g':6},
'e':{'g':3, 'h':4},
'f':{'e':1, 'h':8},
'g':{'h':2},
'h':{'g':2}
}

def dijkstra(graph,start,end):
    # Data required
    distances=defaultdict(lambda: inf)
    distances[start]=0
    parent={}
    not_checked=graph

    # Main loop

    while not_checked:

        # Node in turn with minimal distance

        actual_node=None
        for candidate in not_checked:
            if actual_node==None:
                actual_node=candidate
            elif distances[actual_node]>distances[candidate]:
                actual_node=candidate
        
        # Relaxing paths

        for neighbor in not_checked[actual_node]:
            weight=not_checked[actual_node][neighbor] # In case keys aren't just one element.
            if weight+distances[actual_node]<distances[neighbor]:
                distances[neighbor]=weight+distances[actual_node]
                parent[neighbor]=actual_node

        # Reducing nodes to check
         
        not_checked.pop(actual_node)

    # Returning answer

    if distances[end]==inf:
        print("No path")

    else:
        cur=end
        path=[]
        while cur!=start:
            path.append(cur)
            cur=parent[cur]
        path.append(start)
        print(path[::-1])

dijkstra(graph, 'a', 'h')