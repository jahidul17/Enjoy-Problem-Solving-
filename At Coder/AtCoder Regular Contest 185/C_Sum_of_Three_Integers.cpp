#include <bits/stdc++.h>

using namespace std;

int main()
{

    int n, x, arr[100], ii, jj, kk, i, j, k, l, m;

    cin >> n >> x;

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    for (i = 0; i < n; i++)
    {
        l = i + 1;
        for (j = l; j < n; j++)
        {
            m = j + 1;
            for (k = m; k < n; k++)
            {
                // if (i == n - 1)
                // {
                //     // cout << i << " " << let;
                //     goto endp;
                // }

                if (arr[i] + arr[j] + arr[k] == x)
                {
                    ii = i;
                    jj = j;
                    kk = k;

                    goto summation;
                }
            }
        }
    }

summation:
    cout << ii + 1 << " " << jj + 1 << " " << kk + 1;
    // cout << n;
    // return 0;

    // endp:
    //     cout << "-1";

    return 0;
}
