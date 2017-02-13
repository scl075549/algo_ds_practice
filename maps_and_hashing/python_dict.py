locations = {
    'North America': {'USA': ['Mountain View', 'Atlanta']},
    'Asia': {'China': ['Shanghai'], 'India': ['Bangalore']},
    'Africa': {'Egypt': ['Cairo']}
    }

"""Print the following:
1. A list of all cities in the USA in alphabetic order.
"""
sorted_us_cities = sorted(locations['North America']['USA'])

for city in sorted_us_cities:
    print(city)

"""
2. All cities in Asia, in alphabetic order, next to the name of the country.
"""
asian_countries = locations['Asia']
asian_cities = ['{} - {}'.format(asian_countries[country][0], country) for country in asian_countries]
for city in sorted(asian_cities):
    print(city)

"""Expected output:
Atlanta
Mountain View
Bangalore - India
Shanghai - China
"""
