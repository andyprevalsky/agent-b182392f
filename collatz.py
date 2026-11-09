#!/usr/bin/env python3
"""Print the Collatz sequence starting at 27 and its number of steps."""


def collatz_sequence(n: int) -> list[int]:
    """Return the Collatz sequence from n down to 1, inclusive of both ends."""
    if n < 1:
        raise ValueError("start must be a positive integer")
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main() -> None:
    sequence = collatz_sequence(27)
    for value in sequence:
        print(value)
    # Steps are transitions between numbers, so one fewer than the count of numbers.
    print(f"Total steps: {len(sequence) - 1}")


if __name__ == "__main__":
    main()
