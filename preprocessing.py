import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split


class PreProcessor():
    def __init__(self):
        self.csv_path = "./data/weatherAUS.csv"

    def run(self):
        df = self.load_data()
        return self.split_data(df)

    def load_data(self):
        df = pd.read_csv(self.csv_path)
        # Convert column names to lowecase for convenience
        df.columns = [x.lower() for x in df.columns]

        # Dropping rows with a missing target variable
        df = df.loc[df['raintomorrow'].notnull()]
        return df

    def split_data(self, df):
        # Splitting data early to avoid data leakage
        y = df['raintomorrow']
        X = df.drop(columns=['raintomorrow', 'date'])

        # Splitting in train and test set on 70/30 ratio
        return train_test_split(X, y, test_size=0.3,
                                random_state=123, shuffle=True)

    def get_cat_and_num_cols(self, X_train, X_test):
        self.categorical = [col for col in X_train.columns
                            if X_train[col].dtypes == 'O'
                            and col != 'location']
        # We replace the missing values with an 'Unknown' tag
        for col in self.categorical:
            X_train[col] = X_train[col].replace(np.nan, 'Unknown')

        # Let's also do the same for our test set
        for col in self.categorical:
            X_test[col] = X_test[col].replace(np.nan, 'Unknown')
