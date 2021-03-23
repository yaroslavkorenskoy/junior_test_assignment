import re
from collections import defaultdict

import requests

title = "Clothing Brand"
unitList = ('jackets', 'shirts', 'accessories')
url = 'https://bad-api-assignment.reaktor.com'
urlUnitList = ('/products/', '/availability/')

# Database initialisation
database = defaultdict(dict)
manufBase = set()


# Singleton class should be good practice here, as database in v2.0
def unit_table(unit_type):
    database.clear()
    manufBase.clear()
    # first GET API request
    getData = requests.get(url + urlUnitList[0] + unit_type).json()
    for element in getData:
        manufBase.add(element['manufacturer'])

        database[element['id']].update({'manufacturer': element['manufacturer'],
                                        'name': element['name'],
                                        'color': element['color'],
                                        'price': element['price']})

    # Second GET API request to check availability and add it to the first json db
    for manuf in manufBase:
        getAvailability = requests.get(url + urlUnitList[1] + manuf).json()
        response = getAvailability['response']

        for cur_elem in response:
            availabilityValue = re.findall(r'\>(.*?)\</', cur_elem['DATAPAYLOAD'])
            element = database.get(cur_elem['id'].lower())
            if element is not None:
                element.update(availability=availabilityValue[0])
    return database
