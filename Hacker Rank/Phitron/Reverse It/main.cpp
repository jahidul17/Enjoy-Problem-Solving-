#include <bits/stdc++.h>
using namespace std;

class student
{

public:
    string nm;
    int cls;
    char sec;
    int id;

};
int main()
{
    int n;
    cin>>n;
    student *a=new student[n];

    for(int i=0;i<n;i++){
        cin>>a[i].nm>>a[i].cls>>a[i].sec>>a[i].id;
    }

    int j=n-1;
    for(int i=0;i<n;i++){
        if(j>i){
            swap(a[i].sec,a[j].sec);
        }
        j--;
    }

    for(int i=0;i<n;i++){
        cout<<a[i].nm<<" "<<a[i].cls<<" "<<a[i].sec<<" "<<a[i].id<<endl;
    }


    return 0;
}
