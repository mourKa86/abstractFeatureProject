from abc import ABC, abstractmethod

class Feature(ABC):

    @property
    @abstractmethod
    def apply(self):
        self._apply

    @apply.setter
    def apply(self, value):
        self._apply = value