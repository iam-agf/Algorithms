from dataclasses import dataclass
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

@dataclass
class algorithm:

    @staticmethod
    def dijkstra(graph,start,end):
        '''
        The algorithm needs to preset:
        - A dictionary to save the updated distances between the possible path and the
        starting node
        - A dictionary to save the last updated parent of each node to backtrack the
        final path when the algorithm finisheds
        - A dictionary to know which nodes are still unvisited.
        
        After the preset, the algorithm runs this way:

        1) Find the node with the shortest distance
        2) Update the paths from this node to its possible sons and refresh the
        distance and parents dictionary.
        3) Delete such node from the unvisited nodes

        Finally just backtrack in the parents dictionary to get the final path.
        Here are two possible endings:
        + If the node wasn't connected, the algorithm will end thanks to the unvisited
        dictionary and this will be noticed because the node will have infinite
        distance
        + Else you will have a finite distance and that will mean the parents 
        dictionary can give you the path.
        '''

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

algorithm.dijkstra(graph, 'a', 'h')