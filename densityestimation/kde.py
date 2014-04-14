def kde(sample):
    """Plots a kernel density estimator, kde, based on a user specified kernel and bandwidth.
    
    Plots a kde of a given sample with a user specified kernel and bandwidth, after checking
    if the sample is valid.
    
    ARGS:
        sample: data desired to create a kde for
        
    RETURNS:
        A kde plot is returned based on the sample given, the type of kde desired and the specified
        bandwidth.
    """
    import numpy as np
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
    # Define kernels
    def Gaussian(x):
        return 1/(2*np.pi)**(.5)*np.exp(-x**2/float(2))
    def uniform(x):
        return .5*int(abs(x) <= 1)
    def triangular(x):
        return (1-abs(x))*int(abs(x) <= 1)
    def Epanechnikov(x):
        return 3/float(4)*(1-x**2)*int(abs(x) <= 1)
    # Choose kernel
    kernels = [Gaussian,uniform,triangular,Epanechnikov]
    kernel = ""
    while kernel not in kernels:
        kernel = eval(raw_input("Kernel [Gaussian, uniform, triangular, Epanechnikov]? "))
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
    x_min = min(sample)
    x_max = max(sample)
    x_values = np.linspace(x_min,x_max,100)
    # Define kernel density estimate
    y_values = np.empty(len(x_values))
    counter = 0
    for x in x_values:
        summand = 0
        for u in sample:
            summand += kernel((x-u)/float(h))
        y_values[counter] = summand/float(len(sample)*h)
        counter += 1
    plt.plot(x_values,y_values)
    plt.title("Kernel Density Estimate")
    plt.xlabel("X")
    plt.ylabel("Density")
    plt.show()

