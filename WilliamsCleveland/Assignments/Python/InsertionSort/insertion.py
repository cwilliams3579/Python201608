from datetime import datetime
import time
import random

startTime = time.time()
y = []
for i in range(100):
	y.append(random.randint(0,10000))

def insertion_sort(inserted):
	for i in range(len(inserted)):
		t1 = time.clock()
		temp = inserted[i]
		j = i - 1
		while j >= 0 and inserted[j] >= temp:
			inserted[j+1] = inserted[j]
			j -= 1
		inserted[j+1] = temp
	t2 = time.clock()
	print "Insertion sort took " + str((t2-t1)*1000000)
	return inserted

print insertion_sort(y)
