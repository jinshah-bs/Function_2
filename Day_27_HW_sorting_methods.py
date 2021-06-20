import time
import numpy as np

list_1 = []

for i in range(50):
    list_1.append(i**2)

for i in range(50):
    list_1.append(i**3)

for i in range(50):
    list_1.append(i**4)

for i in range(50):
    list_1.append(i**5)

print(list_1)
start_time1 = time.time()
print(np.sort(list_1, kind="quicksort"))
end_time1 = time.time()
start_time2 = time.time()
print(np.sort(list_1, kind="heapsort"))
end_time2 = time.time()
start_time3 = time.time()
print(np.sort(list_1, kind="mergesort"))
end_time3 = time.time()
start_time4 = time.time()
print(np.sort(list_1, kind="stable"))
end_time4 = time.time()
print("Quicksort = {:.2f}".format((end_time1-start_time1)*1000000000))
print("Heapsort = {:.2f}".format((end_time2-start_time2)*1000000000))
print("Mergesort = {:.2f}".format((end_time3-start_time3)*1000000000))
print("Stable = {:.2f}".format((end_time4-start_time4)*1000000000))
