# -*- coding: utf-8 -*-

import os
import csv
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

glasses = []
glass_params = []
glass_params_vars = {}

"""
glass {
    'id': 1,   
    'Al': '1.1',
    'Ba': '0',
    'Ca': '8.75',
    'Fe': '0',
    'K': '0.06',
    'Mg': '4.49',
    'Na': '13.64',
    'RI': '1.52101',
    'Si': '71.78',
    'Type': '1'
}
"""

def linearize_glass(glass):
    return map(lambda prop: float(prop[1]), filter(lambda prop: prop[0] != 'id' and prop[0] != 'Type', glass.items()))

with open(os.path.join('..', 'data', 'glass.csv'), 'rb') as csv_file:
    reader = csv.reader(csv_file)
    for (num, line) in enumerate(reader):
        if num == 0:
            glass_params = line
            for value in glass_params:
                glass_params_vars[value] = set()
        else:
            glass = {'id': num}
            for (idx, value) in enumerate(line):
                glass[glass_params[idx]] = value
                glass_params_vars[glass_params[idx]].add(value)
            glasses.append(glass)

realCluster = {}
realIdToType = {}
for glass in glasses:
    if realCluster.get(glass.get('Type')) == None:
        realCluster[glass.get('Type')] = []
    realCluster[glass.get('Type')].append(glass.get('id'))
    realIdToType[glass.get('id')] = glass.get('Type')

X = np.array(map(lambda glass: linearize_glass(glass), glasses))

# Кластеризация (K-средних)
kmeans = KMeans(n_clusters=7).fit(X)
kmeansCluster = {}
kmeansIdToType = {}
for glass in glasses:
    group = kmeans.predict([linearize_glass(glass), linearize_glass(glass)])[0]
    if kmeansCluster.get(group) == None:
        kmeansCluster[group] = []
    kmeansCluster[group].append(glass.get('id'))
    kmeansIdToType[glass.get('id')] = group

# Сравнение количества элементов по кластерам
print('Real:')
print(map(lambda cluster: (cluster[0], len(cluster[1])), realCluster.items()))
print('KMeans:')
print(map(lambda cluster: (cluster[0] + 1, len(cluster[1])), kmeansCluster.items()))

kmeansErrorCount = 0

# Снижение размерности пространства
X_reduced = TruncatedSVD(n_components=3).fit_transform(X)

fig = plt.figure(figsize=(16, 8))

ax = fig.add_subplot(121, projection='3d')
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=map(lambda idToType: idToType[1], realIdToType.items()))
ax.set_title("Real Clustering: Truncated SVD reduction (2d) of (9d) data")

ax = fig.add_subplot(122, projection='3d')
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=map(lambda idToType: idToType[1], kmeansIdToType.items()))
ax.set_title("KMeans Clustering: Truncated SVD reduction (2d) of (9d) data")

plt.show()