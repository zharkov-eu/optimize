import os
import csv
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pylab as plt

bouts = []
bout_params = []
bout_params_vars = {}

"""
Bout {
    'age_A': '35',
    'age_B': '27',
    'decision': 'SD',
    'drawn_A': '0',
    'drawn_B': '1',
    'height_A': '179',
    'height_B': '175',
    'judge1_A': '110',
    'judge1_B': '118',
    'judge2_A': '115',
    'judge2_B': '113',
    'judge3_A': '114',
    'judge3_B': '114',
    'kos_A': '33',
    'kos_B': '34',
    'lost_A': '0',
    'lost_B': '1',
    'reach_A': '178',
    'reach_B': '179',
    'result': 'draw',
    'stance_A': 'orthodox',
    'stance_B': 'orthodox',
    'weight_A': '160',
    'weight_B': '160',
    'won_A': '37',
    'won_B': '49'
}
"""

def parse_bout(bout):
    try:
        age_A = int(bout.get("age_A"))
        age_B = int(bout.get("age_B"))
        won_A = int(bout.get("won_A"))
        won_B = int(bout.get("won_B"))
        return [age_A, age_B, won_A, won_B]
    except ValueError:
        return None

with open(os.path.join('..', 'data', 'bouts.csv'), 'rb') as csv_file:
    reader = csv.reader(csv_file)
    for (num, line) in enumerate(reader):
        if num == 0:
            bout_params = line
            for value in bout_params:
                bout_params_vars[value] = set()
        else:
            bout = {}
            for (idx, value) in enumerate(line):
                bout[bout_params[idx]] = value
                bout_params_vars[bout_params[idx]].add(value)
            bouts.append(bout)

X = np.array(filter(lambda bout: bout is not None, map(lambda bout: parse_bout(bout), bouts)))

kmeans = KMeans(n_clusters=3).fit(X)