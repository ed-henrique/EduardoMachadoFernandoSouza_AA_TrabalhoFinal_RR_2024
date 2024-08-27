SHELL := /bin/bash

generate:
	mkdir -p inputs
	python3 generate_inputs.py
	rm inputs/0.txt

compile/dyn:
	gcc -O3 -Wall -Wextra -o dynamic_programming dynamic_programming.c

compile/bb:
	gcc -O3 -Wall -Wextra -o branch_and_bound branch_and_bound.c

compile/greed:
	gcc -O3 -Wall -Wextra -o greedy greedy.c

compile/back:
	gcc -O3 -Wall -Wextra -o backtracking backtracking.c

compile:
	make -j5 compile/dyn compile/bb compile/greed compile/back

bench:
	python3 benchmark.py

plot:
	python3 -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt
	python3 plot.py

clean:
	rm -f dynamic_programming branch_and_bound greedy backtracking logs/* results.csv

