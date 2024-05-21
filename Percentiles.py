import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(f' The 75th percentile for the distribution list is: {x}')

x = numpy.percentile(ages, 90)

print(f' The 90th percentile for the distribution list is: {x}')