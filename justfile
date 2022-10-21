# `just` is a command runner, see https://github.com/casey/just for more

default:
    @just --list

check:
    python ./checker.py ./config.py

fmt:
    black -l 99 ./
