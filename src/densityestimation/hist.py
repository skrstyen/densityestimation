def hist(sample):
    """Plots a histogram based on a user specified origin and bandwidth.
    
    Plots a histogram, a jagged density estimator, of a given sample with a user specified
    origin and bandwidth, after checking if the sample is valid.
    
    ARGS:
        sample: data desired to create a histogram for, entered as a one-dimensional numpy
        array
            origin: any real number
            bandwidth: any number greater than 0
        
    RETURNS:
        A histogram plot is returned based on the sample given, the chosen origin and the specified
        bandwidth.
    """
    import numpy as np
    import math
    import matplotlib.pyplot as plt
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
    # Choose origin
    while True:
        o = raw_input("Origin? ")
        try:
            o = float(o)
            break
        except:
            pass
    # Choose bandwidth
    while True:
        h = raw_input("Bandwidth [>0]? ")
        try:
            h = float(h)
            if h > 0:
                break
        except:
            pass
    # Identify x-axis range
    j_max = int(math.ceil((max(sample)-o)/h))
    j_min = int(math.ceil((min(sample)-o)/h))
    bins = np.arange(j_min,j_max)*h+o
    # Define histogram density estimate and create plot
    y_values = np.zeros(len(bins)-1)
    for i in range(0,len(y_values)):
        for x in sample:
            if bins[i] <= x:
                if x < bins[i+1]:
                    y_values[i] += 1
        y_values[i] = y_values[i]/float(len(sample)*h)
    plt.plot(bins[:-1],y_values)
    plt.title("Histogram Density Estimate")
    plt.xlabel("X")
    plt.ylabel("Density")
    plt.show()
