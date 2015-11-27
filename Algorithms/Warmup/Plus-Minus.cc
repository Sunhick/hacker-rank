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

int main() {
  int n;
  cin >> n;
  vector<int> arr(n);
  int positives = 0, negatives = 0, zeros = 0;
    
  for(int arr_i = 0;arr_i < n;arr_i++) {
    cin >> arr[arr_i];
    if (arr[arr_i] > 0) positives++;
    else if (arr[arr_i] < 0) negatives++;
    else zeros++;
  }
    
  if (n > 0) {
    cout << (float)positives/n << endl;
    cout << (float)negatives/n << endl;
    cout << (float)zeros/n << endl;
  }
  
  return 0;
}
