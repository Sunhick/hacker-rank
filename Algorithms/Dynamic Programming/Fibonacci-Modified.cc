#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

unsigned long long FibModified(unsigned long long first, unsigned long long second, int index) {
  if (index <= 0) return second;
  return FibModified(second, (second*second) + first, index-1);
}

int main() {
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
  unsigned long long first, second, index;
  cin >> first >> second >> index;
  cout << FibModified(first, second, index-2) << endl;

  return 0;
}
