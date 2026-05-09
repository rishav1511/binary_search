import timeit
import matplotlib.pyplot as plt
def merge_sort(arr):
    for i in range(1,len(arr)):
        if len(arr)>1:
            mid=len(arr)//2
            left=arr[:mid]
            right=arr[mid:]
            merge_sort(left)
            merge_sort(right)
            i=j=k=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    arr[k]=left[i]
                    i+=1
                else:
                    arr[k]=right[j]
                    j+=1
                k+=1
            while i<len(left):
                arr[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                arr[k]=right[j]
                j+=1
                k+=1
N=[]
CPU=[]
trail=int(input("enter no of trails: "))
for t in range(trail):
    print("trail no: ",t+1)
    arr=[]
    n=int(input("Enter no of elements: "))
    for i in range(n):
        arr.append(int(input("Enter element: ")))
    start=timeit.default_timer()
    merge_sort(arr)
    stop=timeit.default_timer()
    time=(stop-start)*1000000
    N.append(n)
    CPU.append(round(time,2))
    print("sorted array: ",arr)
    print("time take: ",round(time,2)," microseconds")
print("N CPU")
for t in range(trail):
    print(N[t],CPU[t])
plt.plot(N,CPU)
plt.scatter(N,CPU,marker="*")
plt.xlabel("Array size(n)")
plt.ylabel("CPU time of merge sort")
plt.title("merge sort time efficiency")
plt.show()