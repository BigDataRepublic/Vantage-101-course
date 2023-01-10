import pytest
import pandas as pd

from preprocessing import PreProcessor
from base import Runner


@pytest.fixture
def dummy_data():
    df = pd.read_csv("./data/weatherAUS.csv").head(250)
    yield df


def test_init():
    preproccesor = PreProcessor()

    assert preproccesor is not None
    assert isinstance(preproccesor, Runner)


def test_run():
    preprocessor = PreProcessor()

    preprocessor.run()


def test_load_data():
    preprocessor = PreProcessor()

    result = preprocessor.load_data()

    assert isinstance(result, pd.DataFrame)


def test_split_data(dummy_data):
    preprocessor = PreProcessor()
    dummy_data = preprocessor._prepreprocessing(dummy_data)

    result = preprocessor.split_data(dummy_data)

    isinstance(result, tuple)


def test_set_categorical_cols(dummy_data):
    preprocessor = PreProcessor()

    preprocessor.set_categorical_cols(dummy_data)

    assert preprocessor.categorical is not None
    assert isinstance(preprocessor.categorical, list)


def test_replace_missing_vals(dummy_data):
    preprocessor = PreProcessor()
    preprocessor.set_categorical_cols(dummy_data)

    result = preprocessor.replace_missing_vals(dummy_data)

    assert result.loc[:, preprocessor.categorical].isnull().values.any() == False
