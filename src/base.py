from abc import ABC, abstractclassmethod

import pandas as pd


class Runner(ABC):
    @abstractclassmethod
    def run(self, X: pd.DataFrame):
        pass
