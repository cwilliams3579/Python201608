from datetime import datetime
import time 
import random

startTime = time.time()
def sort():
    
    f = open("sort.txt", "w");
    for i in range(10000):
        f.write( str(random.randrange(1,10000)) + "\n" );
        
    f.close();
    
    
def swapNum( unsorted, index1, index2 ):
    tmp = unsorted[index2]
    unsorted[index2] = unsorted[index1]
    unsorted[index1] = tmp
    
def selection_Sort(a):
    for i in range(len(a)):
        minVal = i
        
        for x in range(i+1, len(a) ):   
            
            if a[x] < a[minVal]:
                minVal = x
 
        swapNum(a, minVal, i)
        
    return a
        
        
sort()
NumList = [int(num) for num in open("sort.txt", "r").readlines()];
sortedList = selection_Sort(NumList)
print len(sortedList), [str(n) + " " for n in sortedList[:100]]
print ('Sorting took {0} second !'.format(time.time() - startTime))
