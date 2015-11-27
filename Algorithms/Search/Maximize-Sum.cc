#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <map>
#include <set>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
  int tt;
  scanf("%d",&tt);
  long long arr[100000];
  long long sum[100000];
  while (tt--) {
    long long n,m;
    scanf("%lld %lld",&n,&m);

    for (int i=0;i<n;i++)
      scanf("%lld",&arr[i]);

    sum[0] = arr[0] % m;

    for (int i=1;i<n;i++)
      sum[i] = (sum[i-1] + arr[i]) % m;

    set <long long> s;
    s.insert(m);
    long long maxi = -1;

    for (int i=0;i<n;i++) {
      set<long long> :: iterator it = s.lower_bound(sum[i]+1);
      long long diff = (sum[i]+m-(*it))%m;
      if (diff > maxi)
	maxi = diff;
      s.insert(sum[i]);
    }
    printf("%lld\n",maxi);
  }
  return 0;
}
