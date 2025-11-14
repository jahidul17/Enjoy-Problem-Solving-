#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    getchar();

    while (t--)
    {
        char input[205];
        fgets(input, sizeof(input), stdin);
        int len = strlen(input);
        if (input[len - 1] == '\n')
            input[len - 1] = '\0';

        int real_size = 0;   // for sizeof()
        int real_strlen = 0; // for strlen()
        int found_null = 0;

        for (int i = 0; input[i] != '\0'; i++)
        {

            if (input[i] == '\\' && input[i + 1] == '0')
            {
                // this is an actual null character in C strings
                real_size++; // count NULL
                if (!found_null)
                    found_null = 1; // strlen stops here
                i++;                // skip '0'
            }
            else
            {
                real_size++; // count regular character
                if (!found_null)
                    real_strlen++; // strlen increments until first NULL
            }
        }

        // sizeof adds one more null character at the end
        real_size += 1;

        printf("%d %d\n", real_size, real_strlen);
    }

    return 0;
}
