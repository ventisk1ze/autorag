from abc import ABC, abstractmethod


class AbstractEngine(ABC):
    """
    Abstract class for inference engine.
    We will define classes for engines using langchain and gpt4all.
    """

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_hyperparams(self):
        pass

    @abstractmethod
    def inference(self):
        pass
