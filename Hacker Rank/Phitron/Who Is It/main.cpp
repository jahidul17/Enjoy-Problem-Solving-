#include <bits/stdc++.h>

using namespace std;

class student
{

public:
    int id;
    char name[100];
    char section;
    float marks;

};

int main()
{
    int test;
    cin>>test;
    while(test>=1)
    {


        student a,b,c;


        cin>>a.id>>a.name>>a.section>>a.marks;
        cin>>b.id>>b.name>>b.section>>b.marks;
        cin>>c.id>>c.name>>c.section>>c.marks;

        //First step
        if(a.marks>=b.marks && a.marks>=c.marks)
        {
            if(a.marks==b.marks)
            {
                if(a.id<b.id)
                {
                    cout<<a.id<<" "<<a.name<<" "<<a.section<<" "<<a.marks<<endl;
                }
                else
                {
                    cout<<b.id<<" "<<b.name<<" "<<b.section<<" "<<b.marks<<endl;
                }

            }
            else if(a.marks==c.marks)
            {
                if(a.id<c.id)
                {
                    cout<<a.id<<" "<<a.name<<" "<<a.section<<" "<<a.marks<<endl;
                }
                else
                {
                    cout<<c.id<<" "<<c.name<<" "<<c.section<<" "<<c.marks<<endl;
                }
            }
            else
            {
                cout<<a.id<<" "<<a.name<<" "<<a.section<<" "<<a.marks<<endl;
            }

        }

        //Second step
        else if(b.marks>=a.marks && b.marks>=c.marks)
        {
            if(b.marks==a.marks)
            {
                if(b.id<a.id)
                {
                    cout<<b.id<<" "<<b.name<<" "<<b.section<<" "<<b.marks<<endl;
                }
                else
                {
                    cout<<a.id<<" "<<a.name<<" "<<a.section<<" "<<a.marks<<endl;
                }

            }
            else if(b.marks==c.marks)
            {
                if(b.id<c.id)
                {
                    cout<<b.id<<" "<<b.name<<" "<<b.section<<" "<<b.marks<<endl;
                }
                else
                {
                    cout<<c.id<<" "<<c.name<<" "<<c.section<<" "<<c.marks<<endl;
                }
            }
            else
            {
                cout<<b.id<<" "<<b.name<<" "<<b.section<<" "<<b.marks<<endl;
            }


        }


        //Third step
        else if(c.marks>=a.marks && c.marks>=b.marks)
        {
            if(c.marks==a.marks)
            {
                if(c.id<a.id)
                {
                    cout<<c.id<<" "<<c.name<<" "<<c.section<<" "<<c.marks<<endl;
                }
                else
                {
                    cout<<a.id<<" "<<a.name<<" "<<a.section<<" "<<a.marks<<endl;
                }

            }
            else if(c.marks==b.marks)
            {
                if(c.id<b.id)
                {
                    cout<<c.id<<" "<<c.name<<" "<<c.section<<" "<<c.marks<<endl;
                }
                else
                {
                    cout<<b.id<<" "<<b.name<<" "<<b.section<<" "<<b.marks<<endl;
                }
            }
            else
            {
                cout<<c.id<<" "<<c.name<<" "<<c.section<<" "<<c.marks<<endl;
            }

        }



        test--;
    }


    return 0;
}
