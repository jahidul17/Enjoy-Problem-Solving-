//Sort It Again
#include <bits/stdc++.h>

using namespace std;

class student
{

public:

    string nm;
    int cls;
    char s;
    long long int id;
    int math_marks;
    int eng_marks;


};

int main()
{
    int n;
    cin>>n;

    student *a=new student[n];

    //Input multiple array
    for(int i=0; i<n; i++)
    {

        cin>>a[i].nm>>a[i].cls>>a[i].s>>a[i].id>>a[i].math_marks>>a[i].eng_marks;

    }


    //Swaping Process
    for(int i=0; i<n-1; i++)
    {

        for(int j=i+1; j<n; j++)
        {

            if(a[i].eng_marks<a[j].eng_marks)
            {
                swap(a[i].math_marks,a[j].math_marks);
                swap(a[i].eng_marks,a[j].eng_marks);
                swap(a[i].nm,a[j].nm);
                swap(a[i].cls,a[j].cls);
                swap(a[i].s,a[j].s);
                swap(a[i].id,a[j].id);
            }

            if(a[i].eng_marks==a[j].eng_marks)
            {
                if(a[i].math_marks<a[j].math_marks)
                {
                    swap(a[i].math_marks,a[j].math_marks);
                    swap(a[i].eng_marks,a[j].eng_marks);
                    swap(a[i].nm,a[j].nm);
                    swap(a[i].cls,a[j].cls);
                    swap(a[i].s,a[j].s);
                    swap(a[i].id,a[j].id);
                }

            }

            if(a[i].math_marks==a[j].math_marks)
            {
                if(a[i].id>a[j].id)
                {
                    swap(a[i].math_marks,a[j].math_marks);
                    swap(a[i].eng_marks,a[j].eng_marks);
                    swap(a[i].nm,a[j].nm);
                    swap(a[i].cls,a[j].cls);
                    swap(a[i].s,a[j].s);
                    swap(a[i].id,a[j].id);
                }

            }


        }

    }


//After descending output
    for(int i=0; i<n; i++)
    {

        cout<<a[i].nm<<" "<<a[i].cls<<" "<<a[i].s<<" "<<a[i].id<<" "<<a[i].math_marks<<" "<<a[i].eng_marks<<endl;

    }


    return 0;
}
