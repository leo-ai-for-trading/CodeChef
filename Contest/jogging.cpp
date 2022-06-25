/*
version of C++: GNU C++17

standard library contain sort:
- #include<bits/stdc++.h> -> it works on C++14


read faster int:
- scanf("%d", &t);
- scanf("%d%d", &n,&k);
- scanf("%s", &s);

read long long int:
- scanf("%lld",&a[i]);

print two integers with new line as separator
- printf("%d %d\n", a, b);

print double on a new line
- printf("%lf\n",d)

shorten the code:
for loop
- #define REP(i,a,b) for (int i = a; i <= b; i++)
*/
#include<stdio.h>
#include<iostream>
#include<vector>
#define rep(i,a,b) for (int i = a; i < b; i++);
typedef long long ll;
using namespace std;
typedef long long int lli;
#define nl "\n";
#define mod 1000000007
ll power(ll a,ll b){
    ll res = 1;
    while (b)
    {
        if (b%2 == 1)
        {
            res = (res*a)%mod;
        }
        a = (a*a)%mod;
        b /= 2;
    }return res;
}

void solve(){
    ll n,x;
    cin>>n>>x;
    ll mul = power(2,n-1);
    ll ans = (mul*x)%mod;
    cout<<ans<<nl;
}

int main(){
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int t;
    cin>>t;
    while (t--)
    {
        solve();
    }
    return 0;
}
