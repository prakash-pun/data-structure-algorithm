# iterable => An iterable is anything that you can loop over using a for loop
# E.g. lists, tuples, strings, sets and dictionaries.

# sequence => A subset of iterables that have: A length, An index, can be sliced
# E.g. lists, strings, tubles

# Examples of iterables that are not seqences => dictionaries, sets, files, generators

countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']

# countries.reverse()

# print(countries)
# countries[::-1]
# print(countries)

for country in reversed(countries):
    print(countries)