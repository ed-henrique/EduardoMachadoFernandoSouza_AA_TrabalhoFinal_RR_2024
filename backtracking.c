#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define CAPACITY 1000

#include <stdio.h>

int knapsack(int W, int w[], int v[], int n) {
    if (n == 0 || W == 0) {
        return 0;
    }

    if (w[n-1] > W) {
        return knapsack(W, w, v, n-1);
    } 
    else {
        int include_item = v[n-1] + knapsack(W - w[n-1], w, v, n-1);
        int exclude_item = knapsack(W, w, v, n-1);
        return (include_item > exclude_item) ? include_item : exclude_item;
    }
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
    int solution = knapsack(CAPACITY, wt, val, n);
    clock_t end = clock();

    double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("%d %.10f\n", solution, time_taken);

    return 0;
}
