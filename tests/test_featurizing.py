import pytest
import pandas as pd

from preprocessing import PreProcessor
from featurizing import Featurizer
from base import Runner


@pytest.fixture
def dummy_data():
    # Probably datasubset would be better here
    X_train, _, _, _ = PreProcessor().run()
    yield X_train


def test_init():
    featurizer = Featurizer()

    assert featurizer is not None
    assert isinstance(featurizer, Runner)


def test_run(dummy_data):
    featurizer = Featurizer()

    result = featurizer.run(dummy_data)

    assert result is not None


def test_create_feature_pipelines(dummy_data):
    featurizer = Featurizer()
    featurizer._set_cat_and_num_cols(dummy_data)

    result = featurizer.create_feature_pipelines()

    assert result is not None
