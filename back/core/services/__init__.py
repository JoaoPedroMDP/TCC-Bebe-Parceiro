#  coding: utf-8
from abc import ABC, abstractmethod


class CrudService(ABC):
    @abstractmethod
    def create(self, command):
        pass

    @abstractmethod
    def patch(self, command):
        pass

    @abstractmethod
    def filter(self, query):
        pass

    @abstractmethod
    def get(self, query):
        pass

    @abstractmethod
    def delete(self, command):
        pass
