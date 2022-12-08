countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Japan']

for index in range(len(countries)):
    print(f'{index+1}. {countries[index]}')

for item in enumerate(countries, start=1):
    print(item)

for index, country in enumerate(countries, start=1):
    print(f'{index}. {country}')

for country in countries:
    print(country)