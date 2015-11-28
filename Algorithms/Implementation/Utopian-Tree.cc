#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

unsigned long long utopian_height(int cycles) {
  unsigned long long height = 1;
  for (int i = 0; i < cycles; i++) {
    if (i % 2) height++;
    else height *= 2;
  }
  return height;
}

int main() {
  int testcases;
  cin >> testcases;

  for(int testcase = 0; testcase < testcases; testcase++) {
    int cycles;
    cin >> cycles;
    auto height = utopian_height(cycles);
    cout << height << endl;
  }

  return 0;
}
