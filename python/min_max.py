countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
populations = [17_500_000, 198_000_000, 10_000_000, 30_000_000, 24_000_000, 128_000_000]


list(zip(countries, populations))
print(min(zip(countries, populations)))
def get_population(pair):
    country, population = pair 
    return population

print(min(zip(countries, populations), key=get_population))
print(min(zip(countries, populations), key=lambda x: x[1]))