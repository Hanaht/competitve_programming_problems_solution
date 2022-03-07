#include <bits/stdc++.h>
using namespace std;
int main(){
    map<string, double>m;
    string t;
    int c;
    double p;
    c=0;
    while (getline(cin,t)){
           c++;
           if (m[t]){
                m[t]+=1;
           }
           else{
            m[t]=1;
           }
           }

    for (auto x:m){
            p = x.second;
            p = (double)p*100/(double)c;
            m[x.first] = p;
    }
    for (auto f:m){
        cout<<f.first<<" "<<setprecision(6)<<f.second << endl;
    }

}