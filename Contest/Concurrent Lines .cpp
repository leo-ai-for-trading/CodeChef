*/
- x/a + y/a = 1
- bx + ay = ab
- (a-x)(b-y) = xy
- map which has prime and its power dividing xy
- calculate separely as xy <= 1e24
- if pq = x then either one of p and q is less than sqrt(x)
- incrementing count of prime divisors
*/


#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long ull ;

vector<pair<ull, ull>> primeFactors(ull n)
{
    vector<pair<ull, ull>> ans ;
    bool flag = 0 ;
    ull c = 0 ;
    while (n % 2 == 0)
    {
        flag = 1 ;
        c++ ;
        n = n/2;
    }
    if ( flag ) ans.push_back({2, c}) ;
 
    for (ull i = 3; i <= sqrt(n); i = i + 2)
    {
        ull c = 0 ;
        bool flag = 0 ;
        while (n % i == 0)
        {
            flag = 1 ;
            c++ ;
            n = n/i;
        }
        if ( flag ) ans.push_back({i, c}) ;
    }

    if (n > 2)
        ans.push_back({n, 1}) ;

    return ans ;
}

int main(){

    ull x, y ;
    cin >> x >> y ;

    vector<pair<ull, ull>> xp = primeFactors(x) ;
    vector<pair<ull, ull>> yp = primeFactors(y) ;

    unordered_map<ull, ull> m ;
    for ( ull i = 0 ; i < xp.size() ; i++ ){
        m[xp[i].first] = xp[i].second ;
    }

    for ( ull i = 0 ; i < yp.size() ; i++ ){
        m[yp[i].first] += yp[i].second ;
    }

    ull ans = 1 ;
    for ( auto val : m ) {
        ans *= ( val.second + 1 ) ;
    }

    cout << ans << endl ;

}
