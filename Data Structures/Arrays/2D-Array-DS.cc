#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    
    signed int ip[6][6];
    signed int  max = -99; //Key Do not initialise to 0
    signed int sum;
   
    for (int i=0; i<6; i++)
        for (int j=0; j<6; j++)
         cin>>ip[i][j];   

    for (int i=0; i<4; i++)
        for (int j=0; j<4; j++)
        {
                sum = ip[i][j] + ip[i][j+1] + ip[i][j+2] + ip[i+1][j+1] + ip[i+2][j] + ip[i+2][j+1] + ip[i+2][j+2];
                if(sum > max) max = sum;
        }
    cout<<max<<endl;
    return 0;
}
