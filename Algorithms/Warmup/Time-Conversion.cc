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
#include <iomanip>

using namespace std;

void split(const string &s, char delim, vector<string> &elems) 
{
  std::stringstream ss(s);
  std::string item;
  while (std::getline(ss, item, delim)) {
    elems.push_back(item);
  }
}

void military_format(string& time) 
{
  vector<string> elems;
  split(time, ':', elems);

  int hr = atoi(elems[0].c_str());
  int min = atoi(elems[1].c_str());
  stringstream ss;
  bool pm = false, found_early = false;

  if (isdigit(elems[2][0])) ss << elems[2][0];
  if (isdigit(elems[2][1])) ss << elems[2][1];
  else found_early = true;

  int sec = atoi(ss.str().c_str());
  if (found_early) {
    if (elems[2][1] == 'p' || elems[2][1] == 'P')
      pm = true;
  }
  if (elems[2][2] == 'p' || elems[2][2] == 'P')
    pm = true;
  
  ss.str("");
  if(pm && hr != 12) hr += 12;
  if (!pm && hr == 12) hr = 0;

  ss << setw(2) << setfill('0') << hr << ":";
  ss << setw(2) << setfill('0') << min << ":";
  ss << setw(2) << setfill('0') << sec ;

  cout << ss.str() << endl;
}

int main()
{
  string time;
  cin >> time;
  military_format(time);
  return 0;
}
