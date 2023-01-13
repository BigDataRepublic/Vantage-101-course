from abc import ABC

from src.base import Runner


def test_runner_init():
    class TestExample(Runner):
        def run(self, X):
            pass

    result = TestExample()

    assert isinstance(result, ABC)
    assert isinstance(result, Runner)
