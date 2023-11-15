#  coding: utf-8
from typing import Dict


class Dictable:
    @staticmethod
    def from_dict(args: Dict):
        """
            Cria uma instância do objeto a partir de um dicionário
            Precisa ser implementado na classe filha
        """
        raise NotImplementedError

    def to_dict(self) -> Dict:
        """
            Serializa o objeto para um dicionário
            Campos None são ignorados
        """
        data = {}
        for key, value in self.__dict__.items():
            if value is not None:
                data[key] = value
        return data
