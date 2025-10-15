#!/usr/bin/env python3
"""Print multiplication table of 2 (1 through 10)."""

def print_table(n: int = 2, upto: int = 10) -> None:
	"""Print multiplication table for n from 1 to upto (inclusive)."""
	for i in range(1, upto + 1):
		print(f"{i} x {n} = {i * n}")


if __name__ == "__main__":
	print_table(2, 10)

