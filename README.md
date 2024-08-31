Find a peak element which is not smaller than its neighbours
Last Updated : 28 Aug, 2024
Given an unsorted array, find a peak element in it. An element is considered to be peak if its value is greater than or equal to the values of its adjacent elements (if they exist). There can be more than one peak elements in an array, we return any of them,

Note: If the array is increasing then just print the last element will be the maximum value.

Example:

Input: arr[]= {5, 10, 20, 15}
Output: 20
Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.

Input: arr[] = {10, 20, 15, 2, 23, 90, 90}
Output: 20 or 90
Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20, similarly 90 has neighbors 23 and 67.

Input: arr[] = [1, 1, 1]
Output : 1
Explanation: All elements are peak in the given array, we can return any of them,

Follow the below steps to Implement the idea: 

If the first element is greater than the second or the last element is greater than the second last, print the respective element and terminate the program.
Else traverse the array from the second index to the second last index i.e. 1 to N – 1  
If for an element array[i] is greater than both its neighbors, i.e., array[i] > =array[i-1]  and array[i] > =array[i+1] , then print that element and terminate.