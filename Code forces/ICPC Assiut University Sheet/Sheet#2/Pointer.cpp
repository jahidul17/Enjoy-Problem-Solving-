#include <stdio.h>
#include <math.h>
void update(int *a, int *b)
{
    int first = *a;
    int second = *b;

    // Complete this function
    *a = first + second;
    *b = first - second;
}

int main()
{
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, abs(b));

    return 0;
}