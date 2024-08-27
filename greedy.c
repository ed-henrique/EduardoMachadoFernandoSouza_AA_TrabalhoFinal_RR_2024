#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define CAPACITY 1000

typedef struct {
    int value;
    int weight;
    double ratio;
} Item;

int compare(const void *a, const void *b) {
    Item *itemA = (Item *)a;
    Item *itemB = (Item *)b;
    return (itemB->ratio > itemA->ratio) - (itemB->ratio < itemA->ratio);
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
        items[i].ratio = (double)items[i].value / items[i].weight;
    }

    fclose(file);

    clock_t start = clock();

    qsort(items, n, sizeof(Item), compare);

    int totalValue = 0, totalWeight = 0;
    for (int i = 0; i < n; i++) {
        if (totalWeight + items[i].weight <= CAPACITY) {
            totalWeight += items[i].weight;
            totalValue += items[i].value;
        } else {
            break;
        }
    }

    clock_t end = clock();

    double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("%d %.10f\n", totalValue, time_taken);

    return 0;
}
