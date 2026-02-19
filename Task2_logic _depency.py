# Independent Events

# Probability of Heads on a coin
P_heads = 1 / 4

# Probability of rolling a 6 on a die
P_eight = 1 / 8

# Independent formula: P(A ∩ B) = P(A) * P(B)
P_independent = P_heads * P_eight

print("Probability of Heads AND rolling a 6:", P_independent)

# Dependent Events (Without Replacement)
# Initial marbles
red = 5
blue = 5
total = red + blue

# First red draw
P_first_red = red / total

# After removing one red
red -= 1
total -= 1

# Second red draw
P_second_red = red / total

# Dependent formula
P_both_red = P_first_red * P_second_red

print("Probability of picking two Red marbles:", P_both_red)