# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import numpy
import array

records = []
N=sys.stdin.readline()
print N

for line in sys.stdin:
    record = [float(field) for field in line.strip().lstrip('[').rstrip(']').split()]
    records.append(record)

#for item in records:
#    print item
#print records(0)
    
print numpy.mean(records)
print numpy.median(records)
print numpy.mode(records)
