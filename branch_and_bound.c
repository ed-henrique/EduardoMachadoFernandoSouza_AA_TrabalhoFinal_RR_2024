#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define CAPACITY 1000

typedef struct {
    int value;
    int weight;
    double ratio;
} Item;

typedef struct {
    int level;
    int profit;
    int weight;
    double bound;
} Node;

double bound(Node u, int n, Item *items) {
    if (u.weight >= CAPACITY) {
        return 0;
    }

    double bound = u.profit;
    int j = u.level + 1;
    int totweight = u.weight;

    while (j < n && totweight + items[j].weight <= CAPACITY) {
        totweight += items[j].weight;
        bound += items[j].value;
        j++;
    }

    if (j < n) {
        bound += (CAPACITY - totweight) * items[j].ratio;
    }

    return bound;
}

int knapsack(int n, Item *items) {
    Node u, v;
    int maxProfit = 0;

    u.level = -1;
    u.profit = 0;
    u.weight = 0;
    u.bound = bound(u, n, items);

    Node stack[n];
    int top = -1;

    stack[++top] = u;

    while (top >= 0) {
        u = stack[top--];

        if (u.level == n - 1) {
            continue;
        }

        v.level = u.level + 1;

        v.weight = u.weight + items[v.level].weight;
        v.profit = u.profit + items[v.level].value;

        if (v.weight <= CAPACITY && v.profit > maxProfit) {
            maxProfit = v.profit;
        }

        v.bound = bound(v, n, items);
        if (v.bound > maxProfit) {
            stack[++top] = v;
        }

        v.weight = u.weight;
        v.profit = u.profit;
        v.bound = bound(v, n, items);
        if (v.bound > maxProfit) {
            stack[++top] = v;
        }
    }

    return maxProfit;
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
    int solution = knapsack(n, items);
    clock_t end = clock();

    double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("%d %.10f\n", solution, time_taken);

    return 0;
}
