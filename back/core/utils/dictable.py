#  coding: utf-8
from typing import Dict


class Dictable:
    @staticmethod
    def from_dict(args: Dict):
        raise NotImplementedError

    def to_dict(self) -> Dict:
        data = {}
        for key, value in self.__dict__.items():
            if value is not None:
                data[key] = value
        return data
