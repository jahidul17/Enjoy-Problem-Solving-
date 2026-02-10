#include <bits/stdc++.h>

using namespace std;

class student
{
public:
    string nm;
    int cls;
    char s;
    int id;
    int math_marks;
    int eng_marks;
};

bool cmp(student c,student d)   //c and d is parameter for this function
{


    if(c.eng_marks>d.eng_marks)
    {
        return true;
    }
    else if(c.eng_marks==d.eng_marks)
    {
        if(c.math_marks>d.math_marks)
        {
            return true;    //When return true it need not sort
        }
        else if(c.math_marks==d.math_marks)
        {
            return c.id<d.id;   //Another way if/else return

        }

        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }



}

int main()
{
    int n;
    cin>>n;

    student *a=new student[n];

    //Group array input
    for(int i=0; i<n; i++)
    {
        cin>>a[i].nm>>a[i].cls>>a[i].s>>a[i].id>>a[i].math_marks>>a[i].eng_marks;
    }

    sort(a,a+n,cmp);


    //After sort output
    for(int i=0; i<n; i++)
    {
        cout<<a[i].nm<<" "<<a[i].cls<<" "<<a[i].s<<" "<<a[i].id<<" "<<a[i].math_marks<<" "<<a[i].eng_marks<<endl;
    }

    return 0;
}
