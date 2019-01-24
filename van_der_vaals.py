import numpy as np

tau = 0.9

def p(fi):
    return -3/fi ** 2 + (8/3 * tau)/(fi - 1/3)


def sol(pi):
    x = np.zeros((3,3), dtype = float)
    x[1,0] = x[2,1] = 1
    x[0,2] = 1/pi
    x[1,2] = -3/pi
    x[2,2] = 1/3 - 8/3 * tau/pi
    roots, vectors = np.linalg.eig(x)
    return(roots)    


def tomin(roots, p, pi_prob):
    vmax = np.amax(roots)
    vmin = np.amin(roots)
    r1 = (vmax - vmin) / 2 * (1 - 1/np.sqrt(3))
    r2 = (vmax - vmin) / 2 * (1 + 1/np.sqrt(3))
    integ = (vmax - vmin) / 2 * (p(r1) + p(r2))
    return integ - (vmax - vmin) * pi_prob 

def search(acc = 1e-04):
    old = np.inf
    while ((new - old) > acc):
        