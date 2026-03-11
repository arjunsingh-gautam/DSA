// Implementing Array in raw form

#include <stdio.h>
int main()
{
    char arr[5] = {'a', 'b', 'c', 'd', 'e'};
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
    {
        printf("Element:%c at address:%d\n", *(arr + i), (arr + i));
    }
    return 0;
}

/*
Output:
Element:a at address:329250679
Element:b at address:329250680
Element:c at address:329250681
Element:d at address:329250682
Element:e at address:329250683

Observation:
    - contiguous memory
    - O(1) Access
    - Sequential and ordered sequence of memory blocks
*/