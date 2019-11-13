import numpy as np
from scipy.sparse import csc_matrix

def pageRank123(G, s = 0.85, maxerr = 0.0001):
    n = G.shape[0]

    # transform G into markov matrix A
    A = csc_matrix(G,dtype=np.float)
    rsums = np.array(A.sum(1))[:,0]
    ri, ci = A.nonzero()
    A.data /= rsums[ri]
    # bool array of sink states
    sink = rsums == 0
    # Compute pagerank r until we converge
    ro, r = np.zeros(n), np.ones(n)
    while np.sum(np.abs(r-ro)) > maxerr:
        ro = r.copy()
        # calculate each pagerank at a time
        for i in range(0,n):
            # inlinks of state i
            Ai = np.array(A[:,i].todense())[:,0]
            # account for sink states
            Di = sink / float(n)
            # account for teleportation to state i
            Ei = np.ones(n) / float(n)
            r[i] = ro.dot( Ai*s + Di*s + Ei*(1-s) )

    # return normalized pagerank
    return r/float(sum(r))


# Example extracted from 'Introduction to Information Retrieval'
G = np.array([[0,0,1,0,0,0,0],
             [0,1,1,0,0,0,0],
             [1,0,1,1,0,0,0],
             [0,0,0,1,1,0,0],
             [0,0,0,0,0,0,1],
             [0,0,0,0,0,1,1],
             [0,0,0,1,1,0,1]])
print pageRank(G, s = 0.86)



    