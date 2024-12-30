from abc import ABC, abstractmethod


class SampleABC(ABC):
    @abstractmethod
    def sample(self):
        pass

    @staticmethod
    def sampleStatic():
        print("Sample Static Method")


class InnerSampleABC1(SampleABC):
    def sample(self):
        print("Inner Sample Method 1")


class InnerSampleABC2(SampleABC):
    def sample(self):
        print("Inner Sample Method 2")


class SampleFactory(ABC):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            print("Initializing Sample Factory")

    @staticmethod
    def createSample(number: int) -> SampleABC:
        if number == 1:
            return InnerSampleABC1()
        elif number == 2:
            return InnerSampleABC2()

factory = SampleFactory()
sample1 = factory.createSample(1)
sample2 = factory.createSample(2)
sample1.sample()
sample2.sample()