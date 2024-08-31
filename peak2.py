#find a peak element using Recursive Binary Search
#"Using binary search, check if the middle element is the peak
# element or not. If the middle element is not he peak element , then check if the
# element on the right side is greater than the middle element then there is always 
# peak element in right side. and vice-verse. Note that both left and right side might have 
# peak element , we just we need to return any peak element
# ollow the steps below to implement the idea:

# Create two variables, l and r, initialize l = 0 and r = n-1
# Recursively perform the below steps till l <= r, i.e. lowerbound is less than the upperbound
# Check if the mid value or index mid = low + (high – low) / 2,  is the peak element or not, if yes then print the element and terminate.
# Else if the element on the left side of the middle element is greater then check for peak element on the left side, i.e. update r = mid – 1
# Else if the element on the right side of the middle element is greater then check for peak element on the right side, i.e. update 
# l=mid+1
# # "


def  findpeakUtil(arr,high,low,n):
    #find index of middle element
    #low+(high-low)/2
    mid=low+(high-low)/2
    mid=int(mid)
    #compare middle with its neighbour
    if(mid==0 or arr[mid-1]<=arr[mid]and
       (mid==n-1 or arr[mid+1]<=arr[mid])):
        return arr[mid]
    #if  middle element is not peak and its right neighbour is greater
    #than it , then rigght half must
    #have a peak element
    else:
        return findpeakUtil(arr,(mid+1),high,n)
 #a Wrapper over recursive function findpeakutil()
def findpeak(arr,n):
    return findpeakUtil(arr,0,n-1,n)
arr=[2,4,6,3,7,2]
n=len(arr)
print(findpeak(arr,n))
