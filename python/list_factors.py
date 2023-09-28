def list_factors(num):
    factors = list(filter(lambda x: num % x == 0, range(1, num)))
    return factors

num = int(input())

factors = list_factors(num)

print(factors)