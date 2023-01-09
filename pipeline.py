from preprocessing import PreProcessor
from featurizing import Featurizer
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline


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


if __name__ == "__main__":
    train_pipeline()
