from abc import ABC
from abc import abstractmethod


class Step(ABC):  # abstract class
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs, utils):  # 必寫(主介面)
        pass


class StepException(Exception):
    pass
