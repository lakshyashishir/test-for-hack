#!/usr/bin/env python3
"""Quick demo script for the test-for-hack sandbox."""


def greet(name: str) -> str:
    return f"Hello, {name}!"


def fibonacci(n: int) -> list[int]:
    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


if __name__ == "__main__":
    print(greet("Nano"))
    print("Fibonacci sequence (10 terms):", fibonacci(10))
