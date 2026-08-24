"""Sum every even number from 1 to 100."""


def sum_even_numbers(start: int = 1, end: int = 100) -> int:
    """Return the sum of even integers in an inclusive range."""
    return sum(n for n in range(start, end + 1) if n % 2 == 0)


if __name__ == "__main__":
    total = sum_even_numbers()
    print(f"Sum of even numbers from 1 to 100: {total}")
