#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<string>
#include<map>
#include<vector>
#include<iomanip>
#define FAST ios::sync_with_stdio(false)
typedef long long ll;
using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--){
        string s;
        cin >> s;
        int k = 0, x = -1;
        while(k < s.size()){
            if((s[k] - '0') % 2){
                if(s[k] == '9' )
                    s[k] -= 1, x = '8';
                else{
                    for(int i = k + 1; i < s.size(); i++)
                        if(s[i] != '4') {
                            if(s[i] > '4') s[k] += 1, x = '0';
                            else s[k] -= 1, x = '8';
                            break;
                        }
                    if(x == -1) s[k] -= 1, x = '8';
                }
                k++; break;
            }
            k++;
        }
        while (k < s.size())
            s[k++] = x;
        x = (s.size() > 1 && s[0] == '0') ? 1 : 0;
        printf("%s\n", s.c_str() + x);
    }
}