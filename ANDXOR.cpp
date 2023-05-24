#include<bits/stdc++.h>
using namespace std;

int addFun(string p, int n)
{
    string s[n];
    for(int i=0;i<n;i++)
    {
        s[i] = p[i]&127;
    }
    for(int i=0;i<n;i++)
    {
        cout<<s[i];
    }
    cout<<endl;
    return 0;
}

int xorFun(string p,int n)
{
    string w[n];
        for(int i=0;i<n;i++)
        {
            w[i] = p[i]^127;
        }
        for(int i=0;i<n;i++)
        {
            cout<<w[i];
        }
        cout<<endl;
        return 0;
}

int main()
{
    string p;
    int n;

    cout<<"Enter the string :";
    cin>>p;

    n=p.size();
    addFun(p,n);
    xorFun(p,n);
}