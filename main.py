def max_num(arr):
    maxnum = arr[0]
    l=len(arr)
    for i in range(l):
        if(maxnum<arr[i]):
            maxnum=arr[i]
    return maxnum

arr=[5,8,9,7,25,65,87]
result=max_num(arr)
print(result)