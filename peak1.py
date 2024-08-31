def findpeak(arr,n):
    #first or last element is peak element
    if(n==1):
        return 0
    if(arr[0]>=arr[1]):
        return 0
    if(arr[n-1]>=arr[n-2]):
        return n-1
    # check for every element
    for i in range(1,n-1):
        #check if the neighbour are smaller
        if (arr[i]>=arr[i-1]and arr[i]>=arr[i+1]):
            return arr[i]
arr=[1,23,46,77,88,9]
n=len(arr)
print(findpeak(arr,n))