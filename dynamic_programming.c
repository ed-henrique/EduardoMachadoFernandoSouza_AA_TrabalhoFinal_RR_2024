#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define CAPACITY 1000

int max(int a, int b) {
    return (a > b) ? a : b;
}

int knapsack(int wt[], int val[], int n) {
    if (!n) {
        return -1;
    }

    int i, w;

    int **K = (int **)malloc((n + 1) * sizeof(int *));
    for (i = 0; i <= n; i++) {
        K[i] = (int *)malloc((CAPACITY + 1) * sizeof(int));
    }

    for (i = 0; i <= n; i++) {
        for (w = 0; w <= CAPACITY; w++) {
            if (i == 0 || w == 0) {
                K[i][w] = 0;
            } else if (wt[i - 1] <= w) {
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
            } else {
                K[i][w] = K[i - 1][w];
            }
        }
    }

    int result = K[n][CAPACITY];

    for (i = 0; i <= n; i++) {
        free(K[i]);
    }
    free(K);

    return result;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <input_size> <input_file>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);

    FILE *file = fopen(argv[2], "r");
    if (!file) {
        printf("Error opening file.\n");
        return 1;
    }

    int val[n], wt[n];
    for (int i = 0; i < n; i++) {
        fscanf(file, "%d,%d", &val[i], &wt[i]);
    }

    fclose(file);

    clock_t start = clock();
    int solution = knapsack(wt, val, n);
    clock_t end = clock();

    double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("%d %.10f\n", solution, time_taken);

    return 0;
}
