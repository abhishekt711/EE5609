import numpy as np
from numpy.linalg import inv
from numpy import linalg as l

M = np.array([[1,0],[0,1],[1/2,3/4]])
c = np.array([[3],[3],[5]])

#Singular Value Decomposition
U, s, V=l.svd(M)

# Diagonalizing S
S = np.zeros(M.shape)
Sinv = S.T
S[:2,:2] = np.diag(s)
sinv = 1./s

#Inverse transpose of S (Moore Penrose Pseudo Inverse)
Sinv[:2,:2] = np.diag(sinv)

#Solution
x = V.T.dot(Sinv).dot(U.T).dot(c)
print(x)
