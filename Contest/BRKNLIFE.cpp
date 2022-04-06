#include <iostream>
using namespace std;
/*
- S_i should be any char except A_j
- we want to prevent A[1,j+1] will become subsequence S[1,j]
*/

int n,m;
string a,s;

bool solv()
{
    int j=0;
    for(int i=0;i<n && j<m;i++){
        if (s[i]=='?'){
            if(a[j]=='e')s[i]='d';
            else s[i]='e';
        
        }else if (s[i]==a[j])j++;
    }
    if (j==m) return 0;
    return 1;
}

int main() {
	int TT=1;cin>>TT;
	for(int tt=1;tt<=TT;tt++){
	    cin>>n>>m;
	    cin>>s>>a;
	    if(solve())cout<<s<<"\n";
	    else cout<<"-1\n";
	}
	
	return 0;
}
