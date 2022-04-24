#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(){
    int test;
    cin >> test;
    while (test--){
        long long n, x, y, c = 0;
        cin >> n;
        int arr[n];
        
        for (int i = 0; i < n; i++){
            cin >> arr[i];
            
            if (arr[i-1] > arr[i] && i >= 1){
                swap(arr[i-1], arr[i]);
                if (arr[i-2] > arr[i-1] && i >= 2){
                    c += 2;
                }
                else{
                    c += 1;
                }
            }
        }
        if (c < 2){
            cout << "YES" << endl;
        }
        else{
            cout << "NO" << endl;
        }
    }
    return 0;
}
