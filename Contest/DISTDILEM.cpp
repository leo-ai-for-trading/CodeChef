/*
- given an arr = [a,b,c,d,e]
- sum of x natural number <= sum of a+b+c+d+e
- x(x+1)/2 <= sum of array2 * sum
- x(x+1) <= 
*/
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while(t--){
        int n;
        int sum=0;
        int temp;
        for (size_t i = 0; i < n; i++)
        {
            cin>>temp;
            sum+=temp;

        }
        int ans=1;
        while ((ans+1)*(ans+2)<=2*sum)
        {
            ans+=1;
        }
        cout<<ans<<endl;
    }

}
