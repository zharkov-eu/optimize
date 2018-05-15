import os
import csv
import matplotlib.pylab as plt

cars = []
car_params = []
car_params_vars = {}

"""
Car {
    'Driven_Wheels': 'rear wheel drive',
    'Engine Cylinders': '6',
    'Engine Fuel Type': 'premium unleaded (required)',
    'Engine HP': '300',
    'MSRP': '40650',
    'Make': 'BMW',
    'Market Category': 'Luxury,Performance',
    'Model': '1 Series',
    'Number of Doors': '2',
    'Popularity': '3916',
    'Transmission Type': 'MANUAL',
    'Vehicle Size': 'Compact',
    'Vehicle Style': 'Convertible',
    'Year': '2011',
    'city mpg': '19',
    'highway MPG': '28'
}
"""

with open(os.path.join('..', 'data', 'car.csv'), 'rb') as csv_file:
    dialect = csv.Sniffer().sniff(csv_file.read(1024))
    csv_file.seek(0)
    reader = csv.reader(csv_file, dialect)
    for (num, line) in enumerate(reader):
        if num == 0:
            car_params = line
            for value in car_params:
                car_params_vars[value] = set()
        else:
            car = {}
            for (idx, value) in enumerate(line):
                car[car_params[idx]] = value
                car_params_vars[car_params[idx]].add(value)
            cars.append(car)

car_params_vars_counter = {}
for key in car_params_vars:
    car_params_vars_counter[key] = {}
    for value in car_params_vars.get(key):
        car_params_vars_counter[key][value] = 0

for car in cars:
    for key in car:
        car_params_vars_counter[key][car[key]] += 1

yearToEngineHp = map(lambda car: {'Model': car['Make'] + ' ' + car['Model'], 'Year': int(car['Year']), 'Engine HP': int(car['Engine HP'])},
                     filter(lambda car: car['Make'] in ('Ferrari', 'Lamborghini'), cars))

""" Leave only first entry of model """
modelFirstReleaseDate = {}
for model in yearToEngineHp:
    current = modelFirstReleaseDate.get(model['Model'])
    if current is None:
        modelFirstReleaseDate[model['Model']] = model
    else:
        current['Year'] = min(current['Year'], model['Year'])

yearToEngineHp = sorted(modelFirstReleaseDate.values(), key=lambda x: x['Year'])

plt.title('Engines HorsePower / Year')
plt.xlabel('Year')
plt.ylabel('Engine HP')

figure, ax = plt.subplots()
for data in yearToEngineHp:
    ax.annotate(data['Model'], xy=(data['Year'], data['Engine HP']), xytext=(data['Year'], data['Engine HP'] + 5))

yearList = map(lambda x: x['Year'], yearToEngineHp)
engineHPList = map(lambda x: x['Engine HP'], yearToEngineHp)

ax.set_xlim([min(yearList) - 2, max(yearList) + 2])
ax.set_ylim([min(engineHPList) - 10, max(engineHPList) + 20])

plt.plot(yearList, engineHPList, 'ro')
