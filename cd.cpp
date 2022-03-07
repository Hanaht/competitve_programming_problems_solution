#include <bits/stdc++.h>
using namespace std;

int main()
{int x,y,a,k,b;
    while(cin>>x>>y){
        if (x!=0 and y!=0){

    unordered_set <int> lst ;


   for (int i=0;i<x;i++){
       cin>>a;
       lst.insert(a);
   }
   for(int j=0;j<y;j++){
       cin>>b;
        lst.insert(b);}


k=lst.size();
//no endline(endl)
cout<<(x+y)-k<<endl;
    }
    else break;}


}