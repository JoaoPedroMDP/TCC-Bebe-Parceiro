#  coding: utf-8
from typing import List

from rest_framework import status


class BenignException(Exception):
    pass


class WithHttpStatusCode(BenignException):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code


class NotFoundError(WithHttpStatusCode):
    def __init__(self, model_class: object):
        message = f"{model_class.__name__} não encontrado"
        super().__init__(message, status.HTTP_404_NOT_FOUND)


class NotCreatedError(WithHttpStatusCode):
    def __init__(self, model_class: object, exception: Exception):
        message = f"{model_class.__name__} não pôde ser criado: {str(exception)}"
        super().__init__(message, status.HTTP_400_BAD_REQUEST)


class ValidationErrors(WithHttpStatusCode):
    def __init__(self, messages: List[str]):
        super().__init__(messages, status.HTTP_400_BAD_REQUEST)
