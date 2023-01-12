import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
import pandas as pd

from preprocessing import PreProcessor
from featurizing import Featurizer


def train_pipeline():
    rfc = RandomForestClassifier()
    preprocessor = PreProcessor()
    featurizer = Featurizer()

    X_train, X_test, y_train, y_test = preprocessor.run()
    y_train = LabelEncoder().fit_transform(y_train)
    featurization_pipeline = featurizer.run(X_train)

    pipe = make_pipeline(featurization_pipeline, rfc)
    print("Model fit")
    pipe.fit(X_train, y_train)
    pickle.dump(pipe, open("./models/rfc.pkl", "wb"))
    X_test.to_csv("./data/X_test.csv")


def predict_pipeline(X_test=None):
    # Assumption that data ispreprocessed already
    if X_test is None:
        # Use dummy data then
        X_test = pd.read_csv("./data/X_test.csv")

    # Use the featurization and model pipeline
    model = pickle.load(open("./models/rfc.pkl", "rb"))
    return model.predict(X_test)
