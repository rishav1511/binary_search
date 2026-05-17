def two_pointer(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        current_sum=arr[left]+arr[right]
        if current_sum==target:
            return left+1,right+1
        elif current_sum<target:
            left+=1
        else:
            right-=1
    return -1
arr=list(map(int,input("Enter your array: ").split()))
target=int(input("Enter target element: "))
result=two_pointer(arr,target)
print(result)
