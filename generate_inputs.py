from random import randint

MIN_PROFIT_LIMIT = 0
MAX_PROFIT_LIMIT = 50

MIN_WEIGHT_LIMIT = 1
MAX_WEIGHT_LIMIT = 30

def main():
    for i in range(1, 1001):
        try:
            f = open(f"inputs/{i}.txt", mode="w")
            for j in range(i):
                random_profit = randint(MIN_PROFIT_LIMIT, MAX_PROFIT_LIMIT)
                random_weight = randint(MIN_WEIGHT_LIMIT, MAX_WEIGHT_LIMIT)
                f.write(f"{random_profit},{random_weight}\n")
            f.close()
        except:
            print(f"Não foi possível criar inputs/{i}.txt")

    for i in range(0, 200000, 1000):
        try:
            f = open(f"inputs/{i}.txt", mode="w")
            for j in range(i):
                random_profit = randint(MIN_PROFIT_LIMIT, MAX_PROFIT_LIMIT)
                random_weight = randint(MIN_WEIGHT_LIMIT, MAX_WEIGHT_LIMIT)
                f.write(f"{random_profit},{random_weight}\n")
            f.close()
        except:
            print(f"Não foi possível criar inputs/{i}.txt")

    for i in range(300000, 1000001, 100000):
        try:
            f = open(f"inputs/{i}.txt", mode="w")
            for j in range(i):
                random_profit = randint(MIN_PROFIT_LIMIT, MAX_PROFIT_LIMIT)
                random_weight = randint(MIN_WEIGHT_LIMIT, MAX_WEIGHT_LIMIT)
                f.write(f"{random_profit},{random_weight}\n")
            f.close()
        except:
            print(f"Não foi possível criar inputs/{i}.txt")

if __name__ == "__main__":
    main()
