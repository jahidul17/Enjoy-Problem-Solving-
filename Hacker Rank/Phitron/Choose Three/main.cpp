#include <iostream>

using namespace std;

int main()
{
    int test;
    cin>>test;

    while(test>=1)
    {


        int n,s;
        int flag=0;
        cin>>n>>s;

        int a[n];

        //Array input
        for(int i=0; i<n; i++)
        {
            cin>>a[i];
        }

        if(n>=3)
        {

            for(int i=0; i<n-2; i++)
            {
                for(int j=i+1; j<n-1; j++)
                {
                    for(int k=j+1; k<n; k++)
                    {
                        if(a[i]+a[j]+a[k]==s)
                        {
                            flag++;
                            break;
                        }
                    }

                    if(flag==1)
                    {
                        break;
                    }

                }
                if(flag==1)
                {
                    break;
                }
            }
            if(flag==1)
            {
                cout<<"YES"<<endl;
            }
            else
            {
                cout<<"NO"<<endl;
            }

        }
        else
        {
            cout<<"NO"<<endl;

        }



        test--;
    }

    return 0;
}
