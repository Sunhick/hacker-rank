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


int main(){
  int testcases;
  cin >> testcases;
    
  for(int testcase = 0; testcase < testcases; testcase++){
    int n; // number of students
    int k; // threshold
        
    int students_count = 0;
        
    cin >> n >> k;
    vector<int> a(n);
    for(int a_i = 0;a_i < n;a_i++){
      cin >> a[a_i];
      if (a[a_i] <= 0) students_count++;
    }
    if (students_count >= k) cout << "NO" << endl; // not cancelled
    else cout << "YES" << endl;
  }
  return 0;
}
