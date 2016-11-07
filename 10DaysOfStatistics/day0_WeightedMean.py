# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

records = []
N=int(sys.stdin.readline())
numerator=0
denominator=0

#Constraints_1: 5<=N<=50
if(N>=5 & N<=50):
    
    for line in sys.stdin:
        record = [int(field) for field in line.strip().lstrip('[').rstrip(']').split()]
        records.append(record)
        
    #Constraints_2: 0<X<=100
    for item in records[0]:
        if (item<0 | item >100):
            records[1].remove(record[0].index(item))
            records[0].remove(item)
            
            
    #Constraints_3: 0<W<=100
    for item in records[1]:
        if (item<0 | item >100):
            records[0].remove(record[1].index(item))
            record[1].remove(item)
            
    for item in records[1]:
        denominator=denominator+item
        #print records[1].index(item)
        #print records[0][records[1].index(item)]
        numerator=numerator+item*records[0][records[1].index(item)]
result=float(numerator/denominator)
print("%.1f" % result)
