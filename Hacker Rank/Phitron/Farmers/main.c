//Solve this programm with chatgpt.

#include <stdio.h>

int main() {
    int T;  // Number of test cases
    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        int M1, M2, D;
        scanf("%d %d %d", &M1, &M2, &D);

        // Calculate the number of fewer days
        double original_days = (double)D;
        double new_days = original_days * (double)M1 / (M1 + M2);
        int fewer_days = D-(int)new_days;

        printf("%d\n", fewer_days);
    }

    return 0;
}
