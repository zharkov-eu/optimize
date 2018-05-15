from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix

X = sparse_random_matrix(1000, 10, density=0.01, random_state=42)
svd = TruncatedSVD(n_components=5, n_iter=7, random_state=42)