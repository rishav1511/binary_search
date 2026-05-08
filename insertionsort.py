import timeit
import matplotlib.pyplot as plt
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=key
N=[]
CPU=[]
trail=int(input("Enter number of trail"))
for t in range(trail):
    print("trail number= ",t+1)
    arr=[]
    n=int(input("Enter number of element"))
    for i in range(n):
        arr.append(int(input("enter element ")))
    start=timeit.default_timer()
    insertion_sort(arr)
    end=timeit.default_timer()
    time=end-start
    N.append(n)
    CPU.append(round(time*1000000,2))
    print("sorted array= ",arr)
    print("time taken= ",round(time,2),"microseconds")
for t in range(trail):
    print(N[t],CPU[t])
plt.plot(N,CPU)
plt.scatter(N,CPU,marker='*')
plt.xlabel("input size")
plt.ylabel("time efficiency insertion sort")
plt.title("innsertion sort time efficiency")
plt.show()

