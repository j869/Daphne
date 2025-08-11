target = int(''.join(bin(ord(c))[2:] for c in input("target: ")), 2)

def generate_exponents(target, max_base, max_exp):
    best_diff = float('inf')  # Initialize with a very large difference
    best_pair = None  # Store the best (a, b) pair
    
    for a in range(2, max_base + 1):  # Start at 2 to skip 1^x
        for b in range(1, max_exp + 1):
            current_value = a ** b
            diff = abs(current_value - target)  # Absolute difference
            
            if diff < best_diff:  # Check if this is the closest so far
                best_diff = diff
                best_pair = (a, b)
                #print(f"New best pair: {best_pair}, Difference: {best_diff}")
    
    return best_pair  # Return the best (a, b) pair after all checks

# Example call
while target >= 10**10 or target <= -10**10:
    best_a, best_b = generate_exponents(target, 499, 500) 
    print(f"Best pair: base={best_a}, exponent={best_b}, Difference: {abs(best_a**best_b - target)}")
    target = best_a**best_b-target  # Update target for the next iteration
print(target)