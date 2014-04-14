def nnde(sample):
     """Plots a nearest-neighbor density estimator, nnde, based on a user specified k.
    
    Plots a nnde of a given sample with a user specified k, after checking
    if the sample is valid.
    
    ARGS:
        sample: data desired to create a nnde for
        
    RETURNS:
        A nnde plot is returned based on the sample given, the chosen k.
    """
    import numpy as np
    import math
    import matplotlib.pyplot as plt
    %matplotlib inline
    import sys
    # Test sample
    try:
        sample = np.array(sample)
    except:
        print "That is not a valid sample."
        sys.exit()
    isArray = True
    if len(sample.shape) != 1:
        isArray = False
    for u in sample:
        try:
            float(u)
        except:
            isArray = False
    if isArray == False:
        print "That is not a valid sample."
        sys.exit()
    # Choose  k
    k0 = int(np.floor(np.sqrt(len(sample))))
    while True:
        k = raw_input("Order [%d]? "%(k0))
        try:
            k = int(k)
            break
        except:
            pass
    # Identify x-axis range
    x_min = min(sample)
    x_max = max(sample)
    x_values = np.linspace(x_min,x_max,100)
    # Define nearest-neighbor density estimate
    y_values = np.empty(len(x_values))
    counter = 0
    for x in x_values:
        delta = [abs(x - u) for u in sample]
        delta.sort()
        y_values[counter] = (k-1)/float(2*len(sample)*delta[k-1])
        counter += 1
    plt.plot(x_values,y_values)
    plt.title("Nearest-Neighbor Density Estimate")
    plt.xlabel("X")
    plt.ylabel("Density")
    plt.show()