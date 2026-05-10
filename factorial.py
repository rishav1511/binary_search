import timeit
import matplotlib.pyplot as plt
def factorial(n):
    if n==1 or n==0:
        return 2
    else:
        return n*factorial(n-1)
N=[]
CPU=[]
print("Number \t factorial \t time")
number=[5,10,15,20,25]
for n in number:
    start=timeit.default_timer()
    result=factorial(n)
    stop=timeit.default_timer()
    t=stop-start
    N.append(n)
    CPU.append(t)
    print(n,"\t",result,"\t",t)
plt.plot(N,CPU)
plt.scatter(N,CPU,marker="*")
plt.xlabel("Input number(n)")
plt.ylabel("execution time")
plt.title("factorial using recursion")
plt.show()