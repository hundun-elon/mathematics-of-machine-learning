# finding the eigen values for huge matrices is painful;
# let's use python packages for help.

import numpy as np
from sympy import Matrix



def eigen_space(A):
      # eigenvalues and their corresponding eigenspaces

      eigen_data = A.eigenvects()

      # eigenvalues with their algebraic multiplicity and eigenspaces
      eigenspaces = []
      for e_val, mult, basis in eigen_data:
            eigenspaces.append({
                  "eigenvalue": e_val,
                  "multiplicity": mult,
                  "eigenspace_basis": basis
            })
      return eigenspaces
# example using this module.


# A = Matrix([
#     [0, -1, 1, 1],
#     [-1, 1, -2, 3],
#     [2, -1, 0, 0],
#     [1, -1, 1, 0]
# ])
# print(eigen_space(A))

# make it exportable
if __name__=='__main__':
      A= None #change this into your matrix.
      eigen_space(A)

