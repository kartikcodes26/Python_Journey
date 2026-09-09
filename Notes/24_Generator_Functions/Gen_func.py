import tracemalloc

tracemalloc.start()

# Code goes here

def gen_func(num):
    for i in range(num):
        yield(i**3)


# num_cubes = [x**3 for x in range(1000000)]
num_cubes = gen_func(1000000)

current, peak = tracemalloc.get_traced_memory()




















tracemalloc.stop()

print(f"Current Memory Usage : {(current / (1024 * 1024)):.4f} MB")
print(f"Peak Memory Usage : {(peak / (1024 * 1024)):.4f} MB")
