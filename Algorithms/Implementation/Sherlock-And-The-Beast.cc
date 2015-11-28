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

string GenerateNumber(int fives, int threes) {
  stringstream ss;
  if (fives == 0 && threes == 0) return "-1";
  for (int i = 0; i < fives; i++) ss << "5";  
  for (int i = 0; i < threes; i++) ss << "3";

  return ss.str();
}

string FindNumber(int digits) {
  // Initially all digits are 555....<digit times>
  int fives = digits;
  int threes = 0;

  if (!(fives % 3)) return GenerateNumber(fives, threes);

  // inject group of 5 3's from left to right
  for (int i = 0; (i + 5) <= digits; i += 5) {
    fives -= 5;
    if (fives < 0) return "-1";
    if (!(fives % 3) && !((digits - fives) % 5)) break;
  }

  threes =  digits - fives;
  if (threes < 0 || threes % 5) return "-1";
  if (fives < 0 || fives % 3) return "-1";
  
  return GenerateNumber(fives, threes);
}

int main() {
  int testcases;
  cin >> testcases;
  for(int testcase = 0; testcase < testcases; testcase++){
    int digits;
    cin >> digits;
    auto num = FindNumber(digits);
    cout << num << endl;
  }
  return 0;
}
