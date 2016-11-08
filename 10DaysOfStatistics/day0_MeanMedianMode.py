# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import numpy
import array
from scipy import stats

record = []
N=int(sys.stdin.readline())
if(N>=10 & N<=2500):
    
    for line in sys.stdin:
        record = [int(field) for field in line.strip().lstrip('[').rstrip(']').split()]

    for item in record:
        if (item<0 | item >100000):
            record.remove(item)
    #numpyArray = numpy.array(record)

    print numpy.mean(record)
    print numpy.median(record)
    print min(stats.mode(record)[0])
