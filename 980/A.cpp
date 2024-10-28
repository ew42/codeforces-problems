#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int t;
  cin >> t;
  while (t--) {
    int a, b;
    cin >> a >> b;

    if (a >= b) {
      cout << a << endl;
    }
    else {
      int minRequired = max(0, b - a);
      if (a > minRequired) {
        cout << a - minRequired << endl;
      }
      else {
        cout << 0 << endl;
      }
    }
  }
}
