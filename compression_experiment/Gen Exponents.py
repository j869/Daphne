# This script generates all combinations of base and exponent from 1 to 500
# and writes the results to a file named 'exponents.txt'.

# Open a file in write mode ('w')
with open('exponents.txt', 'w') as file:
    for a in range(1, 501):       # Base from 1 to 500
        for b in range(1, 501):   # Exponent from 1 to 500
            try:
                result = a ** b   # Compute a^b
                file.write(f"{a}^{b} = {result}\n")  # Write to file
            except OverflowError:  # Handle extremely large numbers
                file.write(f"{a}^{b} = Too large (overflow)\n")