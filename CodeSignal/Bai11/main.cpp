#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int CheckLucky(int n , int a[],int i)
{
    if (n <= 0)
    {
        int sum1 = 0;
        int sum2 = 0;
        for(int j = 0 , z =i/2; j<i/2 ;j++ , z++)
        {
            sum1 += a[j];
            sum2 += a[z];
        }
        if(sum1 == sum2 )
            cout<<"true";
        else
            cout<<"false";
        return 0;
    }
    a[i] = n%10;
    n = n/10;
    i++;
    return CheckLucky(n,a,i);
}

int main()
{
    int a[123456];
    CheckLucky(239017,a,0);
    return 0;
}
