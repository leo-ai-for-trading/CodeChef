\*
- most significant bit
- the xor of two same number will be = 0
- the most significant bit decides what is greater or smaller
- comparing two number the one with most significant bit is the 1 that you find first in the two numbers
  10101 -> the 1 is the most significant because it is the first and the second number contains 0 first
  01010
*\

#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int getmsb(int n)
{
    if (n == 0)
        return 0;
    int msb = 0;
    n = n/2;
    while(n!=0){
        n = n/2;
        msb++;
    }
    return msb;
}

int main() {
	// your code goes here
	int t;
	cin >> t;
	while(t--){
	    int n;
	    cin >>n;
	    vector<int> a(n),msbc(32,0);
	    for (int i = 0;i<n;i++){
	        cin >> a[i];
	        int msb = getmsb(a[i]);
	        msbc[msb]++;
	    }
	   int64_t pairs = 0;
	   for (int i = 0;i<n;i++){
	       int msb = getmsb(a[i]);
	       pairs += max(0,msbc[msb]-1);
	   }
	   cout << pairs /2  <<endl;
	}
	return 0;
}
