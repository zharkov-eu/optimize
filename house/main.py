import os
import csv
import numpy as np
from scipy.optimize import minimize
from scipy.interpolate import Rbf
import matplotlib.pylab as plt
from mpl_toolkits import mplot3d
from house_enums import *
from house import House, house_filter

houses = []
house_params = []

with open(os.path.join('..', 'data', 'house.csv'), 'rb') as csv_file:
    reader = csv.reader(csv_file)
    for (num, line) in enumerate(reader):
        if num == 0:
            house_params = line
        else:
            house = {}
            for (idx, value) in enumerate(line):
                house[house_params[idx]] = value
            houses.append(House(house))

houseFilter = House({
    # "GarageType": GarageType.NoGarage.value,
    "PoolQC": PoolQC.NoPool.value
})

housesFiltered = filter(lambda house: house_filter(house, houseFilter), houses)

lotArea = map(lambda house: house.LotArea, housesFiltered)
overallCond = map(lambda house: house.OverallCond, housesFiltered)
overallQual = map(lambda house: house.OverallQual, housesFiltered)
firstFlrSF = map(lambda house: house.FirstFlrSF, housesFiltered)
secondFlrSF = map(lambda house: house.SecondFlrSF, housesFiltered)
lowQualFinSF = map(lambda house: house.LowQualFinSF, housesFiltered)
salePrice = map(lambda house: house.SalePrice, housesFiltered)

coordinatesMap = {}

for idx, price in enumerate(salePrice):
    coordinate = (lotArea[idx], overallCond[idx], overallQual[idx], firstFlrSF[idx], secondFlrSF[idx], lowQualFinSF[idx])
    if coordinatesMap.has_key((coordinate)):
        coordinatesMap[coordinate] = (price + coordinatesMap.get(coordinate)) / 2
    coordinatesMap[coordinate] = price

coordinates = list(coordinatesMap.keys())
coordinateSalePrices = list(coordinatesMap.values())

interpolated = Rbf(
    zip(*coordinates)[0], zip(*coordinates)[1], zip(*coordinates)[2],
    zip(*coordinates)[3], zip(*coordinates)[4], zip(*coordinates)[5],
    coordinateSalePrices
)

initial = np.array([np.average(lotArea), np.average(overallCond), np.average(overallQual),
                    np.average(firstFlrSF), np.average(secondFlrSF), np.average(lowQualFinSF)])
bounds = (
    (min(lotArea), max(lotArea)),
    (max(1, min(overallCond)), max(1, max(overallCond))),
    (max(1, min(overallQual)), max(1, max(overallQual))),
    (max(20, min(firstFlrSF)), max(20, max(firstFlrSF))),
    (max(20, min(secondFlrSF)), max(20, max(secondFlrSF))),
    (min(lowQualFinSF), max(lowQualFinSF))
)

result = minimize(
    lambda x: interpolated(x[0], x[1], x[2], x[3], x[4], x[5]).item(),
    initial, method="SLSQP", bounds=bounds
)

# fig = plt.figure()
# ax = plt.axes(projection="3d")
# ax.view_init(30, 35)
# ax.plot3D(overallCond, overallQual, salePrice, 'ro')

# plt.plot(lotAreaToSalePrice[0], lotAreaToSalePrice[1], lotAreaToSalePrice[2], 'ro')