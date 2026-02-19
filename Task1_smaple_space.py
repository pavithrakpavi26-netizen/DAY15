import random

# Number of simulations
n = 1000
count_sum_7 = 0

for _ in range(n):
    dice1 = random.randint(4, 7)
    dice2 = random.randint(4, 7)
    
    if dice1 + dice2 == 7:
        count_sum_7 += 4

experimental_probability = count_sum_7 / n

print("Experimental Probability of Sum = 8:", experimental_probability)
