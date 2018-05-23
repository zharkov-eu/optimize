# -*- coding: utf-8 -*-

import os
import csv
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.cluster import AffinityPropagation, DBSCAN, KMeans
from sklearn.decomposition import FactorAnalysis, PCA, TruncatedSVD
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

irises = []
iris_params = []
iris_params_vars = {}

"""
iris {
    'Id': '1',
    'PetalLengthCm': '1.4',
    'PetalWidthCm': '0.2',
    'SepalLengthCm': '5.1',
    'SepalWidthCm': '3.5',
    'Species': 'Iris-setosa'
}
"""

species_enum = {
    'Iris-versicolor': 0,
    'Iris-setosa': 1,
    'Iris-virginica': 2
}

def linearize_iris(iris):
    return map(lambda prop: float(prop[1]), filter(lambda prop: prop[0] != 'Id' and prop[0] != 'Species', iris.items()))

def cluster_info(cluster, linearize_irises):
    predictions = cluster.fit_predict(linearize_irises)
    predictCluster = {}
    predictIdToType = {}
    for (idx, iris) in enumerate(irises):
        group = predictions[idx]
        if predictCluster.get(group) == None:
            predictCluster[group] = []
        predictCluster[group].append(iris.get('Id'))
        predictIdToType[iris.get('Id')] = group
    return {'predictCluster': predictCluster, 'predictIdToType': predictIdToType}

with open(os.path.join('..', 'data', 'iris.csv'), 'rb') as csv_file:
    reader = csv.reader(csv_file)
    for (num, line) in enumerate(reader):
        if num == 0:
            iris_params = line
            for value in iris_params:
                iris_params_vars[value] = set()
        else:
            iris = {}
            for (idx, value) in enumerate(line):
                iris[iris_params[idx]] = value
                iris_params_vars[iris_params[idx]].add(value)
            irises.append(iris)

realCluster = {}
realIdToType = {}
for iris in irises:
    if realCluster.get(species_enum.get(iris.get('Species'))) == None:
        realCluster[species_enum.get(iris.get('Species'))] = []
    realCluster[species_enum.get(iris.get('Species'))].append(iris.get('Id'))
    realIdToType[iris.get('Id')] = species_enum.get(iris.get('Species'))

X = np.array(map(lambda iris: linearize_iris(iris), irises))

# Кластеризация (K-средних)
kmeans = KMeans(n_clusters=3).fit(X)
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
ax.set_title("Real Clustering: TruncatedSVD reduction (3d) of (4d) data")

trunk_fig_kmean = plt.figure()
ax = trunk_fig_kmean.add_subplot(111, projection='3d')
ax.scatter(X_truncated[:, 0], X_truncated[:, 1], X_truncated[:, 2], c=kmeansClassification)
ax.set_title("KMeans Clustering: TruncatedSVD reduction (3d) of (4d) data")

trunk_fig_affinity = plt.figure()
ax = trunk_fig_affinity.add_subplot(111, projection='3d')
ax.scatter(X_truncated[:, 0], X_truncated[:, 1], X_truncated[:, 2], c=affinityClassification)
ax.set_title("Affinity Clustering: TruncatedSVD reduction (3d) of (4d) data")

trunk_fig_dbscan = plt.figure()
ax = trunk_fig_dbscan.add_subplot(111, projection='3d')
ax.scatter(X_truncated[:, 0], X_truncated[:, 1], X_truncated[:, 2], c=dbscanClassification)
ax.set_title("DBSCAN Clustering: TruncatedSVD reduction (3d) of (4d) data")

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