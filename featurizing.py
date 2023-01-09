import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import RobustScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer


class Featurizer():
    def __init__(self):
        self.categorical = None
        self.numerical = None

    def run(self, X):
        if self.categorical is None:
            self._get_cat_and_num_cols(X)
        return self.create_feature_pipelines()

    def create_feature_pipelines(self):
        # Create a one-hot encoder for categorical variables
        encoder = OneHotEncoder(handle_unknown='error',
                                drop='first', sparse=True)
        # And then add it to the pipeline for categorical variables
        cat_transformer = Pipeline(steps=[('onehot', encoder)])

        imputer = SimpleImputer(missing_values=np.nan, strategy="median")
        # Initiate a scaler as well for scaling our continuous variables
        scaler = RobustScaler()
        num_transformer = Pipeline(steps=[
            ('imputer', imputer),
            ('scaler', scaler)
        ])

        # Finally combining both categorical
        # and numerical pipelines into one final object
        featurize_pipeline = ColumnTransformer(
            transformers=[
                ('num', num_transformer, self.numerical),
                ('cat', cat_transformer, self.categorical)
            ], remainder='passthrough')
        return featurize_pipeline

    def _get_cat_and_num_cols(self, X_train):
        # Defining our categorical and numerical variables
        self.categorical = [var for var in X_train.columns
                            if X_train[var].dtype == 'O']
        self.numerical = [var for var in X_train.columns
                          if X_train[var].dtype != 'O']
