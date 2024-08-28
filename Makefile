SHELL := /bin/bash

generate:
	mkdir -p inputs
	python3 generate_inputs.py
	rm inputs/0.txt

compile/dyn:
	gcc -O3 -Wall -Wextra -o dynamic_programming dynamic_programming.c

compile/greed:
	gcc -O3 -Wall -Wextra -o greedy greedy.c

compile:
	make -j5 compile/dyn compile/greed

bench:
	python3 benchmark.py

plot:
	python3 -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt
	python3 plot.py

clean/bin:
	rm -f dynamic_programming greedy

clean:
	rm -f dynamic_programming greedy logs/* assets/plot.svg results.csv

