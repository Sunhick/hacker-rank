#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

long long xor_sum(vector<long long> array) {
  long long xorsum = 0;
  long long N = array.size();

  for (int i = 0, p = 1; i < 32; i++, p <<= 1) {
    int c = 0;

    for (int j = 0; j < N; j++)
      if (array[j] & p) c++;

    xorsum += (long long) c * (N - c + 1) * p;
  }

  return xorsum;
}

int main() {
  int testcases;
  cin >> testcases;

  for (int i = 0; i < testcases; i++) {
    long long size;
    cin >> size;
    vector<long long> array(size);

    cin >> array[0];

    for (long long i = 1; i < size; i++) {
      cin >> array[i];
      array[i] ^= array[i-1];
    }

    auto xsum = xor_sum(array);
    cout << xsum << endl;
  }
    
  return 0;
}
