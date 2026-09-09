import random

# 1. random.random()
# Returns a random floating-point number in the range [0.0, 1.0)
float_val = random.random()

# 2. random.uniform(a, b)
# Returns a random floating-point number N such that a <= N <= b
float_range = random.uniform(1, 10)

# 3. random.randint(a, b)
# Returns a random integer N such that a <= N <= b (inclusive of both endpoints)
dice_roll = random.randint(1, 6)

# 4. random.choice(sequence)
# Returns a single random element from a non-empty sequence (e.g., list, tuple)
greeting = random.choice(["Hello", "Hi", "Hey", "Howdy"])

# 5. random.choices(sequence, weights=None, k=1)
# Returns a list of k elements chosen from the sequence with replacement.
# Allows optional weighting for probabilities.
roulette_results = random.choices(
    population=["Red", "Black", "Green"], weights=[18, 18, 2], k=10
)

# 6. random.shuffle(x)
# Shuffles the sequence x in-place (modifies the original list directly)
deck = list(range(1, 53))
random.shuffle(deck)

# 7. random.sample(population, k)
# Returns a list of k unique elements chosen from the population without replacement
hand = random.sample(deck, k=5)
