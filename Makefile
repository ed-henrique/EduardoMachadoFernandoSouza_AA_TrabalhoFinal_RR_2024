SHELL := /bin/bash

generate:
	mkdir -p inputs
	python3 generate_inputs.py
	rm inputs/0.txt

compile/dyn:
	gcc -O3 -Wall -Wextra -o dynamic_programming dynamic_programming.c

compile/back:
	gcc -O3 -Wall -Wextra -o backtracking backtracking.c

compile:
	make -j2 compile/dyn compile/back

bench:
	python3 benchmark.py

plot:
	python3 -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt
	python3 plot.py

clean/bin:
	rm -f dynamic_programming backtracking

clean:
	rm -f dynamic_programming backtracking logs/* assets/plot.svg results.csv

