#include <bits/stdc++.h>

using namespace std;

int main()
{

    int a, b;
    float c;
    cin >> a >> b;
    c = a / (float)b;
    cout << "floor " << a << " / " << b << " = " << floor(c) << endl;
    cout << "ceil " << a << " / " << b << " = " << ceil(c) << endl;
    cout << "round " << a << " / " << b << " = " << round(c) << endl;
    return 0;
}