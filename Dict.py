__author__ = 'pointschan'

cities = {'CA': 'San Francisco', 'MI': 'Detroit',
            'FL': 'Jacksonville', 'ON': 'Toronto'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

# ok pay attention!
cities['_find'] = find_city

#find_city is function, assign function to cities['_find']



# this line is the most important ever! study
# cities['_find'] - function call with 2 args, a list 'cities' and states to be searched

city_found = cities['_find'](cities, 'CA')
print city_found

city_found = cities['_find'](cities, 'ON')
print city_found

city_found = cities['_find'](cities, 'FL')
print city_found

city_found = cities['_find'](cities, 'OR')
print city_found


