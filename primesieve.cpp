#include <vector>
#include <iostream>

using namespace std;
vector<bool> mark(100000001,true);

void sieve(int n)
{
    int count = 0;
    int p = 2;
    while(p*p <= n)
    {
        if (mark[p])
        {
            for (int i=2*p; i<=n; i+=p)
                mark[i] = false;
        }
        p++;
    }

    for (int i=2; i<=n;i++)
        count += mark[i];
    cout << count << endl;
}

int main()
{
    mark[0] = false;
    mark[1] = false;
    int n,q,x;
    cin >> n;
    cin >> q;
    sieve(n);
    for (int i=0; i<q; i++)
    {
        cin >> x;
        cout << mark[x] << endl;
    }
}
