import abc

class IAccountant(abc.ABC):
    @abc.abstractmethod
    def step(self, noise_multiplier: float, sample_rate: float):
        pass