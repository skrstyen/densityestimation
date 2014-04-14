==================
Density Estimation
==================

This package provides functions for three specific types of density estimators.  
You might find it most useful for tasks involving plotting kernel density estimates, 
histograms and nearest-neighbor density estimates.

Typical intallation often looks like this::

    !pip install densityestimation

    from densityestimation import kde
    from densityestimation import hist
    from densityestimation import nnde


Dependencies
============

* Numpy

* Matplotlib

* Math


Examples
========

| import numpy as np
| sample = np.random.normal(0,1,1000)
| kde(sample) 
|
| import numpy as np
| sample = np.random.normal(0,1,1000)
| hist(sample)
|
| import numpy as np
| sample = np.random.normal(0,1,1000)
| nnde(sample)

