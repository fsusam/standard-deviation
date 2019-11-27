import statistics
import numpy as np

sample = [1, 2, 3, 4, 5]


print("Standard Deviation of the sample is % s " 
                    %(statistics.stdev(sample))) 

print("Variance of the sample is % s" 
     %(statistics.variance(sample))) 


print("Mean of the sample is % s" 
     %(statistics.mean(sample)))  

print("Median of the sample is % s" 
     %(statistics.median(sample)))

print("quartiles of the sample is % s" 
     %(np.percentile(sample, [25, 50, 75] , interpolation = 'midpoint')))
