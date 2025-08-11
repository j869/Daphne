# This script generates all combinations of base 1-499 and exponent 1-500
# and writes the results to a file named 'exponents.csv'.
# my laptop miscalculates anything more then base 499.


def generate_exponents(filename, max_base=499, max_exp=500):
    """Generate exact exponents in a^b format to specified file"""
    with open(filename, 'w', encoding='utf-8') as f:
        for a in range(2, max_base + 1):  # Start at 2 to skip 1^x
            for b in range(1, max_exp + 1):
                f.write(f"{a},{b},{a**b}\n")

# Example usage:
if __name__ == "__main__":
    generate_exponents("exponents.txt")