// Author : Sunil BN
// Copyright : Copyright 2015, hacker_rank Project
// License : MIT
// Version : 1.0.0
// Email : sunhick@gmail.com

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int count_squares(int a, int b) {
  int counter;
  // Intermediate value theorem
  // https://www.mathsisfun.com/algebra/intermediate-value-theorem.html
  // https://en.wikipedia.org/wiki/Intermediate_value_theorem
  int sqrta = (int)(ceil(sqrt(a)));
  int sqrtb = (int)(floor(sqrt(b)));
  counter = sqrtb - sqrta + 1;     
  return counter;
}

int main() {
  int testcases;
  cin >> testcases;

  int a, b;
  for (int i = testcases; i > 0; i--) {
    cin >> a >> b;
    cout << count_squares(a, b) << endl;
  }

  return 0;
}
