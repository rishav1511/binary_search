import timeit
import matplotlib.pyplot as plt
import random
def matrix_mutiply(A,B,n):
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j]+=A[i][k]*B[k][j]
    return C
N=[]
CPU=[]
sizes=[5,10,15,20,25]
print("matrix \t time in seconds")
print("--------------------------")
for n in sizes:
    A=[[random.randint(1,10) for _ in range(n)]for _ in range(n)]
    B=[[random.randint(1,10) for _ in range(n)]for _ in range(n)]
    start=timeit.default_timer()
    matrix_mutiply(A,B,n)
    stop=timeit.default_timer()
    time=(stop-start)*1000000
    N.append(n)
    CPU.append(round(time,5))
    print(n,"x",n,"\t\t",round(time,5))
plt.plot(N,CPU)
plt.scatter(N,CPU,marker="*")
plt.xlabel("Matrix size(n*n)")
plt.ylabel("Execution time")
plt.title("Matrix multiplication time efficiency")
plt.show()
    