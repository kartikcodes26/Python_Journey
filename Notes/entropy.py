import random

random.seed(97)
a = [4, "Asus", 'z', False, 7.13]
print(random.randint(1,20))
print(random.choice(a))

random.shuffle(a)
print(a)

subset = random.sample(a, k=2)
print(subset)

