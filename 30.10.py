import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

a = 0
b = 1

def data_generation():
    tau = 0.5
    mu = 0.5
    sigma = 0.2
    n = 1000
    
    x_n = stats.norm.rvs(loc=mu, scale=sigma, size=int(tau*n))
    x_u = stats.uniform.rvs(loc=a, scale=b-a, size=int((1-tau)*n))
    x = np.concatenate((x_u, x_n))
    return x

def t_ij(x, tau, mu, sigma):
    """T_ij(x, theta)"""
    p_in = stats.norm.pdf(x, loc = mu, scale = sigma)
    p_iu = stats.uniform.pdf(x, loc = a, scale = b-a)
    p = tau * p_in + (1-tau) * p_iu
    t_in = tau * p_in / p
    t_iu = (1-tau) * p_iu / p
    return t_in, t_iu

def update_theta(x, tau, mu, sigma):
    """Iterate theta"""
    t_n, t_u = t_ij(x, tau, mu, sigma)
    tau = np.sum(t_n) / x.size
    mu = np.sum(t_n * x) /  np.sum(t_n)
    sigma = np.sqrt(np.sum(t_n * (x - mu)**2) /  np.sum(t_n))
    return tau, mu, sigma

def em(x, tau, mu, sigma, eps=1e-3):
    """tau, mu, sigma are initiial astimations, returns theta"""
    new = (tau, mu, sigma)
    rtol = 1e-3
    while True:
        old = new
        new = update_theta(x, *old)
        if np.allclose(new, old, rtol = rtol, atol = 0):
            break
    return new
    
def main():
    x = data_generation()
    plt.hist(x, bins=100)
    tau, mu, sigma = 0.7, 0.1, 0.1
    tau, mu, sigma = em(x, tau, mu, sigma)
    print (tau, mu, sigma)
    
if __name__ == '__main__':
    main()