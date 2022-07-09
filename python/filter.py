# use a hashtable to filter out duplicate items
# define a set off items that we want to reduce duplicates

items = ["apple", "peer", "orange", "banana", "apple", "orange", "apple",
         "pear", "banana", "orange", "apple", "kiwi", "pear", "apple", "orange"]

# Create a hashtable to perform a filter

filter = dict()

# loop over each time and add to the hashtable
for key in items:
    filter[key] = 0

# create a set from the resulting keys in the hashtable
result = set(filter.keys())
print(result)
