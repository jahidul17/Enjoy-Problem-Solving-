#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, q;
    cin >> n >> q;

    vector<vector<int>> arr(n);

    // for (int i = 0; i < n; i++)
    // {
    //     int size;
    //     cin >> size;

    //     arr[i].resize(size);

    //     for (int j = 0; j < size; j++)
    //     {
    //         cin >> arr[i][j];
    //     }
    // }

    // for (int k = 0; k < q; k++)
    // {
    //     int i, j;
    //     cin >> i >> j;

    //     cout << arr[i][j] << endl;
    // }

    for (auto &row : arr)
    {
        int size;
        cin >> size;
        row.resize(size);
        for (auto &element : row)
        {
            cin >> element;
        }
    }

    for (int i = 0; i < q; i++)
    {
        int o, p;
        cin >> o >> p;
        cout << arr[o][p] << endl;
    }

    return 0;
}