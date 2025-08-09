"""
compression_experiment.py

This script demonstrates converting text to a large integer and representing it as a mathematical formula.
"""

def text_to_int(text):
    """Convert text to a large integer using UTF-8 bytes."""
    return int.from_bytes(text.encode('utf-8'), 'big')

def int_to_formula(n):
    """
    Represent the integer as a sum of powers (very basic example).
    """
    terms = []
    base = 1000
    while n > 0:
        exp = 0
        while base ** (exp + 1) <= n:
            exp += 1
        coeff = n // (base ** exp)
        terms.append(f"{coeff}*{base}^{exp}")
        n -= coeff * (base ** exp)
    return ' + '.join(terms)

def main():
    text = "Hello, world!"
    n = text_to_int(text)
    print(f"Text: {text}")
    print(f"As integer: {n}")
    formula = int_to_formula(n)
    print(f"As formula: {formula}")

if __name__ == "__main__":
    main()
