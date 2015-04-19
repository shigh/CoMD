import numpy as np

def computeIJ(Tfl, Trw):
    read = 0.0
    write = 0.0
    flop = 0.0

    # compute tmp: 1 / r^2
    # => read position vectors of atoms i & j
    read += 6.0 * Trw
    flop += 9.0 * Tfl

    # compute tmp: (sigma)^6 * (1 / r^2)^3
    flop += 8.0 * Tfl

    # compute tmp: potential
    flop += 3.0 * Tfl

    # update potentials of atoms i & j
    read += 2.0 * Trw
    flop += 2.0 * 2.0 * Tfl
    write += 2.0 * Trw

    # compute magntitude of force
    flop += 6.0 * Tfl

    # update force vectors of atoms i & j
    # => NOT counting read position vectors
    read += 6.0 * Trw
    flop += 6.0 * 2.0 * Tfl
    write += 6.0 * Trw

    # contribute to system potential
    flop += Tfl

    return read + flop + write

def modelLJ(grid, length):
    '''
    Parameters
    '''
    Tfl = 1.0 / (2300 * 1e6)        # BW Users Guide
    Trw = 0.011467 * 1e-6           # STREAM

    sigma = 2.315
    Rcutoff = 2.5 * sigma
    
    nb = 4                          # number of atoms in basis
    nx = grid[0]
    ny = grid[1]
    nz = grid[2]

    minDim = np.array([0.0, 0.0, 0.0])
    maxDim = np.array([nx*length, ny*length, nz*length])

    nAtoms = nb * nx * ny * nz
    #nintIJ = 20                     # periodic lattice! ADDING
    #timeIJ = computeIJ(Tfl, Trw)
    #runtime = nAtoms * (nintIJ / 2.0) * timeIJ
    return 0

nx = 10
ny = 10
nz = 10
grid = (nx, ny, nz)
length = 3.65
runtime = modelLJ(grid, length)
print "%i x %i x %i: %1.2f (s)" % (nx, ny, nz, runtime)
