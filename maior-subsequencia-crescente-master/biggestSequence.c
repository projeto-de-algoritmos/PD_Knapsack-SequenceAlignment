// A Naive C recursive implementation
#include <stdio.h>
#include <stdlib.h>
 
int _lis(int arr[], int n, int* max_ref)
{
    // Base case
    if (n == 1)
        return 1;
 
    // 'max_ending_here' is length of LIS
    // ending with arr[n-1]
    int res, max_ending_here = 1;
 
    for (int i = 1; i < n; i++) {
        res = _lis(arr, i, max_ref);
        if (arr[i - 1] < arr[n - 1]
            && res + 1 > max_ending_here)
            max_ending_here = res + 1;
    }
 
    if (*max_ref < max_ending_here)
        *max_ref = max_ending_here;
    
    return max_ending_here;
}
 
int lis(int arr[], int n)
{
    int max = 1;
 
    _lis(arr, n, &max);
    
    return max;
}

int subSequence(int n){
    
}
 
int main()
{
    int arr[] = { 10,9,2,5,3,7,101,18 };
    int n = sizeof(arr) / sizeof(arr[0]);
 
    // Function call
    printf("Length of lis is %d and n is %d\n", lis(arr, n), n);
    return 0;
}