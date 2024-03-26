//a code to demonstrate the use of the package

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import uniform
from scipy.stats import expon
from scipy.stats import poisson
from scipy.stats import binom
from scipy.stats import geom
from scipy.stats import nbinom
from scipy.stats import hypergeom

# Normal distribution
data = norm.rvs(size=1000)
plt.hist(data, bins=30, density=True)
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Normal distribution')
plt.show()

# Uniform distribution
data = uniform.rvs(size=1000)
plt.hist(data, bins=30, density=True)
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Uniform distribution')
plt.show()

# Exponential distribution
data = expon.rvs(size=1000)
plt.hist(data, bins=30, density=True)
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Exponential distribution')
plt.show()

# Poisson distribution
data = poisson.rvs(mu=3, size=1000)
plt.hist(data, bins=30, density=True)
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Poisson distribution')
plt.show()

# Binomial distribution
data = binom.rvs(n=10, p=0.5, size=1000)
plt.hist(data, bins=30, density=True)
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Binomial distribution')
plt.show()

# Geometric distribution
data = geom.rvs(p=0.5, size=1000)
plt.hist(data, bins=30, density=True)
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Geometric distribution')
plt.show()

# Negative binomial distribution
data = nbinom.rvs(n=10, p=0.5, size=1000)
plt.hist(data, bins=30, density=True)
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Negative binomial distribution')
plt.show()

# Hypergeometric distribution
data = hypergeom.rvs(M=20, n=7, N=12, size=1000)
plt.hist(data, bins=30, density=True)
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Hypergeometric distribution')
plt.show()
# When I run the code, I get the following error:
# ```
# Traceback (most recent call last):
#   File "example.py", line 1, in <module>
#     import numpy as np
# ModuleNotFoundError: No module named 'numpy'
