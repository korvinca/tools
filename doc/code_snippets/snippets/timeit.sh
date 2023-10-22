#!/bin/bash
set -x
python -m timeit -s "variable=False" "if variable == True: pass"
python -m timeit -s "variable=False" "if variable is True: pass"
python -m timeit -s "variable=False" "if variable: pass"