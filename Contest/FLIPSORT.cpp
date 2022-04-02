*/
- x - lenght
- x shoud be unique 

10101110 take the full substring and convertit
01010001 first char is successfully converted now flip the remaining substring
00101110 and so on
00010001 until...
00000001 
for every position containing 1 flip(i, n - 1) this allows that x stay unique; print the size of the vector and i and x separate by a vector
/*

using namespace std;

int main()
{
  int t;
  cin >> t;
  while (t--)
  {
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector < pair<int, int> > ops;
    for (int i = 0; i < n; i++)
    {
      if (s[i] == '1')
      {
        ops.push_back({i + 1, n - i});
        \\flip the string
        for (int j = i; j < n; j++)
        {
          if (s[j] == '1')
            s[j] = '0';
          else
            s[j] = '1';
        }
     }
   }
   cout << ops.size() << "\n";
   for (auto [x,y]: ops) {
      cout << x << " " << y << "\n";
    }
   }
   return 0;
 }
