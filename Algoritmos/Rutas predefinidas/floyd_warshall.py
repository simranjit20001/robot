import networkx as nx
import numpy as np
"""Floyd-Warshall algorithm for shortest paths.
"""
#    Copyright (C) 2004-2015 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.
__author__ = """Aric Hagberg <aric.hagberg@gmail.com>"""
__all__ = ['floyd_warshall',
           'floyd_warshall_predecessor_and_distance',
           'floyd_warshall_numpy']


def floyd_warshall_numpy(G, nodelist=None, weight='weight'):
    """Find all-pairs shortest path lengths using Floyd's algorithm.

    Parameters
    ----------
    G : NetworkX graph

    nodelist : list, optional
       The rows and columns are ordered by the nodes in nodelist.
       If nodelist is None then the ordering is produced by G.nodes().

    weight: string, optional (default= 'weight')
       Edge data key corresponding to the edge weight.

    Returns
    -------
    distance : NumPy matrix
        A matrix of shortest path distances between nodes.
        If there is no path between to nodes the corresponding matrix entry
        will be Inf.

    Notes
    ------
    Floyd's algorithm is appropriate for finding shortest paths in
    dense graphs or graphs with negative weights when Dijkstra's
    algorithm fails.  This algorithm can still fail if there are
    negative cycles.  It has running time O(n^3) with running space of O(n^2).
    """
    try:
        import numpy as np
    except ImportError:
        raise ImportError(\
          "to_numpy_matrix() requires numpy: http://scipy.org/ ")


    # To handle cases when an edge has weight=0, we must make sure that
    # nonedges are not given the value 0 as well.
    A = nx.to_numpy_matrix(G, nodelist=nodelist, multigraph_weight=min,
                              weight=weight, nonedge=np.inf)
    n,m = A.shape
    I = np.identity(n)
    A[I==1] = 0 # diagonal elements should be zero
    for i in range(n):
        A = np.minimum(A, A[i,:] + A[:,i])
    return A


def floyd_warshall_predecessor_and_distance(G, weight='weight'):
    """Find all-pairs shortest path lengths using Floyd's algorithm.

    Parameters
    ----------
    G : NetworkX graph

    weight: string, optional (default= 'weight')
       Edge data key corresponding to the edge weight.

    Returns
    -------
    predecessor,distance : dictionaries
       Dictionaries, keyed by source and target, of predecessors and distances
       in the shortest path.

    Notes
    ------
    Floyd's algorithm is appropriate for finding shortest paths
    in dense graphs or graphs with negative weights when Dijkstra's algorithm
    fails.  This algorithm can still fail if there are negative cycles.
    It has running time O(n^3) with running space of O(n^2).

    See Also
    --------
    floyd_warshall
    floyd_warshall_numpy
    all_pairs_shortest_path
    all_pairs_shortest_path_length
    """
    from collections import defaultdict
    # dictionary-of-dictionaries representation for dist and pred
    # use some defaultdict magick here
    # for dist the default is the floating point inf value
    dist = defaultdict(lambda : defaultdict(lambda: float('inf')))
    for u in G:
        dist[u][u] = 0
    pred = defaultdict(dict)
    # initialize path distance dictionary to be the adjacency matrix
    # also set the distance to self to 0 (zero diagonal)
    undirected = not G.is_directed()
    for u,v,d in G.edges(data=True):
        e_weight = d.get(weight, 1.0)
        dist[u][v] = min(e_weight, dist[u][v])
        pred[u][v] = u
        if undirected:
            dist[v][u] = min(e_weight, dist[v][u])
            pred[v][u] = v
    for w in G:
        for u in G:
            for v in G:
                if dist[u][v] > dist[u][w] + dist[w][v]:
                    dist[u][v] = dist[u][w] + dist[w][v]
                    pred[u][v] = pred[w][v]
    return dict(pred),dict(dist)




def floyd_warshall(G, weight='weight'):
    """Find all-pairs shortest path lengths using Floyd's algorithm.

    Parameters
    ----------
    G : NetworkX graph

    weight: string, optional (default= 'weight')
       Edge data key corresponding to the edge weight.


    Returns
    -------
    distance : dict
       A dictionary,  keyed by source and target, of shortest paths distances
       between nodes.

    Notes
    ------
    Floyd's algorithm is appropriate for finding shortest paths
    in dense graphs or graphs with negative weights when Dijkstra's algorithm
    fails.  This algorithm can still fail if there are negative cycles.
    It has running time O(n^3) with running space of O(n^2).

    See Also
    --------
    floyd_warshall_predecessor_and_distance
    floyd_warshall_numpy
    all_pairs_shortest_path
    all_pairs_shortest_path_length
    """
    # could make this its own function to reduce memory costs
    return floyd_warshall_predecessor_and_distance(G, weight=weight)[1]


# fixture for nose tests


def setup_module(module):
    from nose import SkipTest
    try:
        import numpy
    except:
        raise SkipTest("NumPy not available")


"""-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
------------------------------------------------------------------------------"""








np.random.seed(0)
G=nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27])
G.add_edge(1, 2, weight=3 )
G.add_edge(2, 3, weight=4 )
G.add_edge(3, 4, weight=3 )
G.add_edge(4, 5, weight=7 )
G.add_edge(4, 6, weight=3 )
G.add_edge(6, 7, weight=4 )
G.add_edge(6, 12, weight=5)
G.add_edge(6, 11, weight=6 )
G.add_edge(6, 18, weight=10 )
G.add_edge(6, 24, weight=10 )
G.add_edge(7, 8, weight=4)
G.add_edge(7, 10, weight=5)
G.add_edge(8, 9, weight=5)
G.add_edge(24, 26, weight=4)
G.add_edge(24, 25, weight=4)
G.add_edge(24, 27, weight=11)
G.add_edge(24, 27, weight=11)
G.add_edge(11, 12, weight=1)
G.add_edge(12, 13, weight=2)
G.add_edge(13, 17, weight=3)
G.add_edge(13, 14, weight=7)
G.add_edge(16, 17, weight=4)
G.add_edge(16, 15, weight=10)
G.add_edge(15, 14, weight=3)
G.add_edge(18, 19, weight=2)
G.add_edge(20, 18, weight=5)
G.add_edge(19, 21, weight=3)
G.add_edge(22, 21, weight=7)
G.add_edge(22, 23, weight=3)
path_lengths=nx.floyd_warshall(G, weight='weight')




print(nx.shortest_path(G))
