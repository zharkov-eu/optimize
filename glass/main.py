# -*- coding: utf-8 -*-

import os
import csv
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.cluster import AffinityPropagation, DBSCAN, KMeans
from sklearn.decomposition import FactorAnalysis, PCA, TruncatedSVD
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

def cluster_info(cluster, linearize_glasses):
    predictions = cluster.fit_predict(linearize_glasses)
    predictCluster = {}
    predictIdToType = {}
    for (idx, glass) in enumerate(glasses):
        group = predictions[idx]
        if predictCluster.get(group) == None:
            predictCluster[group] = []
        predictCluster[group].append(glass.get('id'))
        predictIdToType[glass.get('id')] = group
    return {'predictCluster': predictCluster, 'predictIdToType': predictIdToType}

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
kmeansCluster = cluster_info(kmeans, X)
kmeansConfusion = confusion_matrix(map(lambda x: int(x), realIdToType.values()), kmeansCluster.get('predictIdToType').values())

# Кластеризация (AffinityPropagation)
affinity = AffinityPropagation().fit(X)
affinityCluster = cluster_info(affinity, X)
affinityConfusion = confusion_matrix(map(lambda x: int(x), realIdToType.values()), affinityCluster.get('predictIdToType').values())

# Кластеризация (DBSCAN)
dbscan = DBSCAN().fit(X)
dbscanCluster = cluster_info(dbscan, X)
dbscanConfusion = confusion_matrix(map(lambda x: int(x), realIdToType.values()), dbscanCluster.get('predictIdToType').values())

# Сравнение количества элементов по кластерам
print('Real:')
print(map(lambda cluster: (cluster[0], len(cluster[1])), realCluster.items()))
print('KMeans:')
print(map(lambda cluster: (cluster[0], len(cluster[1])), kmeansCluster.get('predictCluster').items()))
print('AffinityCluster:')
print(map(lambda cluster: (cluster[0], len(cluster[1])), affinityCluster.get('predictCluster').items()))
print('DBSCAN Cluster:')
print(map(lambda cluster: (cluster[0], len(cluster[1])), dbscanCluster.get('predictCluster').items()))

# Матрица ошибок
print('KMeans:')
print(kmeansConfusion)
print('AffinityCluster:')
print(affinityConfusion)
print('DBSCAN Cluster:')
print(dbscanConfusion)

# Снижение размерности пространства:
realClassification = map(lambda idToType: idToType[1], realIdToType.items())
kmeansClassification = map(lambda idToType: idToType[1], kmeansCluster.get('predictIdToType').items())
affinityClassification = map(lambda idToType: idToType[1], affinityCluster.get('predictIdToType').items())
dbscanClassification = map(lambda idToType: idToType[1], dbscanCluster.get('predictIdToType').items())

# Снижение размерности пространства: TruncatedSVD
X_truncated = TruncatedSVD(n_components=3).fit_transform(X)

trunk_fig = plt.figure()
ax = trunk_fig.add_subplot(111, projection='3d')
ax.scatter(X_truncated[:, 0], X_truncated[:, 1], X_truncated[:, 2], c=realClassification)
ax.set_title("Real Clustering: TruncatedSVD reduction (3d) of (9d) data")

trunk_fig_kmean = plt.figure()
ax = trunk_fig_kmean.add_subplot(111, projection='3d')
ax.scatter(X_truncated[:, 0], X_truncated[:, 1], X_truncated[:, 2], c=kmeansClassification)
ax.set_title("KMeans Clustering: TruncatedSVD reduction (3d) of (9d) data")

trunk_fig_affinity = plt.figure()
ax = trunk_fig_affinity.add_subplot(111, projection='3d')
ax.scatter(X_truncated[:, 0], X_truncated[:, 1], X_truncated[:, 2], c=affinityClassification)
ax.set_title("Affinity Clustering: TruncatedSVD reduction (3d) of (9d) data")

trunk_fig_dbscan = plt.figure()
ax = trunk_fig_dbscan.add_subplot(111, projection='3d')
ax.scatter(X_truncated[:, 0], X_truncated[:, 1], X_truncated[:, 2], c=dbscanClassification)
ax.set_title("DBSCAN Clustering: TruncatedSVD reduction (3d) of (9d) data")

plt.show()

# Снижение размерности пространства: Pricipal Component Analysis
X_factor = PCA(n_components=3).fit_transform(X)

pca_fig = plt.figure()
ax = pca_fig.add_subplot(111, projection='3d')
ax.scatter(X_factor[:, 0], X_factor[:, 1], X_factor[:, 2], c=realClassification)
ax.set_title("Real Clustering: PCA reduction (3d) of (9d) data")

pca_fig_kmean = plt.figure()
ax = pca_fig_kmean.add_subplot(111, projection='3d')
ax.scatter(X_factor[:, 0], X_factor[:, 1], X_factor[:, 2], c=kmeansClassification)
ax.set_title("KMeans Clustering: PCA reduction (3d) of (9d) data")

pca_fig_affinity = plt.figure()
ax = pca_fig_affinity.add_subplot(111, projection='3d')
ax.scatter(X_factor[:, 0], X_factor[:, 1], X_factor[:, 2], c=affinityClassification)
ax.set_title("Affinity Clustering: PCA reduction (3d) of (9d) data")

pca_fig_dbscan = plt.figure()
ax = pca_fig_dbscan.add_subplot(111, projection='3d')
ax.scatter(X_factor[:, 0], X_factor[:, 1], X_factor[:, 2], c=dbscanClassification)
ax.set_title("DBSCAN Clustering: PCA reduction (3d) of (9d) data")

plt.show()

# Снижение размерности пространства: Factor Analysis
X_factor = FactorAnalysis(n_components=3).fit_transform(X)

factor_fig = plt.figure()
ax = factor_fig.add_subplot(111, projection='3d')
ax.scatter(X_factor[:, 0], X_factor[:, 1], X_factor[:, 2], c=realClassification)
ax.set_title("Real Clustering: Factor Analysis reduction (3d) of (9d) data")

factor_fig_kmean = plt.figure()
ax = factor_fig_kmean.add_subplot(111, projection='3d')
ax.scatter(X_factor[:, 0], X_factor[:, 1], X_factor[:, 2], c=kmeansClassification)
ax.set_title("KMeans Clustering: Factor Analysis reduction (3d) of (9d) data")

factor_fig_affinity = plt.figure()
ax = factor_fig_affinity.add_subplot(111, projection='3d')
ax.scatter(X_factor[:, 0], X_factor[:, 1], X_factor[:, 2], c=affinityClassification)
ax.set_title("Affinity Clustering: Factor Analysis reduction (3d) of (9d) data")

factor_fig_dbscan = plt.figure()
ax = factor_fig_dbscan.add_subplot(111, projection='3d')
ax.scatter(X_factor[:, 0], X_factor[:, 1], X_factor[:, 2], c=dbscanClassification)
ax.set_title("DBSCAN Clustering: Factor Analysis reduction (3d) of (9d) data")

plt.show()