# Bayes Theorem: P(Spam | Free)

# Given probabilities
P_spam = 0.75            # P(Spam)
P_ham = 0.07             # P(Ham)
P_free_given_spam = 0.75 # P(Free | Spam)
P_free_given_ham = 0.07  # P(Free | Ham)

# Step 1: Calculate total probability of P(Free)
P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)

# Step 2: Apply Bayes' Theorem
P_spam_given_free = (P_free_given_spam * P_spam) / P_free

# Step 3: Print result
print("P(Free) =", round(P_free, 3))
print("P(Spam | Free) =", round(P_spam_given_free, 3))

# Convert to percentage
print("Probability email is Spam if it contains 'Free':",
      round(P_spam_given_free * 100, 2), "%")

