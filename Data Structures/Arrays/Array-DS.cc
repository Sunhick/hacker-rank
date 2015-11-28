#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    
    int n; //Size of Array
    cin>>n;
    int *ip = (int*)calloc(n, sizeof(int));
    int *op = (int*)calloc(n, sizeof(int));
    for(int i = 0;i<n ; i++)
    {
        scanf("%d",&ip[i]);
        op[n-1-i] = ip[i];
    }
    for(int j=0;j<n;j++)
    cout<<op[j]<< " ";
    cout<<endl;
    return 0;
}

