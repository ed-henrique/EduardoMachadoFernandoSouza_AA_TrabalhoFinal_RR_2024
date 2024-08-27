#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define CAPACITY 1000

typedef struct {
    int value;
    int weight;
} Item;

void knapsack(int i, int currentWeight, int currentValue, int *maxValue, int n, Item *items) {
    if (i == n) {
        if (currentValue > *maxValue) {
            *maxValue = currentValue;
        }
        return;
    }

    knapsack(i + 1, currentWeight, currentValue, maxValue, n, items);

    if (currentWeight + items[i].weight <= CAPACITY) {
        knapsack(i + 1, currentWeight + items[i].weight, currentValue + items[i].value, maxValue, n, items);
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

    Item *items = (Item *)malloc(n * sizeof(Item));
    for (int i = 0; i < n; i++) {
        fscanf(file, "%d,%d", &items[i].value, &items[i].weight);
    }

    fclose(file);

    clock_t start = clock();
    int solution = 0;
    knapsack(0, 0, 0, &solution, n, items);
    clock_t end = clock();

    double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("%d %.10f\n", solution, time_taken);

    return 0;
}
