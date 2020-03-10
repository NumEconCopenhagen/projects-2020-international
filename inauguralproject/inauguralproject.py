import numpy as np #import numpy module 

# a. initial global variables 

N = 10000 # Number of Individuals 
w = np.linspace(0.5, 1.5, 10) # Uniform wage between 0.5 and 1.5 distributed by number of individuals
L = np.linspace(0, 1, 10) # Labor Supply 


# b. Constructing the utility function 
def util_func(L, c, e=0.3, v=10): # e = elasticity of labor supply, v = scale of disutility of labor, c = consumption 
    '''Utility Function that will be used to find the optimal value of consumption and Labour that will yield maximum utility'''
    
    u = np.log(c) - v*((L**(1 + 1/e)/(1 + 1/e)))
    return u 

# c. Constructing the expenditure function 
def resources(L, m=1, t0=0.4, t1=0.1, k=0.4): # m = cash-on-hand, t0= standard labor income tax, t1=top bracket labor tax, k = cutoff of labor income tax 
    '''Function that calculates the total resources within an economy'''
    
    x = m + wL + (t0*w*L + t1*max(w*L- k, 0))
    return L_now, x 

# d. optimized values of c* and l* 


    





# e. importing plotting packages and creating settings
%matplotlib inline
import matplotlib.pyplot as plt # import matplotlib module 
from mpl_toolkits.mplot3d import Axes3D # for making 3d plots 
plt.style.use('seaborn-whitegrid') # Personal styling of plot 

# f. create 3d figure
fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection='3d')
ax.plot_surface(c,L,w,cmap=cm.jet)

# g. adding labels to 3d chart
ax.set_xlabel('$c*$')
ax.set_ylabel('$l*$')
ax.set_zlabel('$w$')

# h. invert xaxis
ax.invert_xaxis()

# I. Calculating total tax revenue 

def total_tax(L_opt, w, t0=0.4, t1=0.1, k=0.4):
     ''' Function calculating the total tax revenue one recieves from a population of 10,000 people  '''
    T = 0
    
    for w_now, L_now in zip(w, L):
    T += t0*w_now*L_now + t1*max(w_now* - k, 0)
