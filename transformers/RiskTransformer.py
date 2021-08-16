import numpy as np

class RiskTransformer(object):

    def __init__(self):
        pass

    def transform_output(self, X, feature_names):
        X = np.array(X)
        return X * 2