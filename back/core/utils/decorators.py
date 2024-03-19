#  coding: utf-8
from rest_framework import status
from rest_framework.response import Response

from config import ENV
from core.utils.exceptions import HttpFriendlyError


def endpoint(func):
    def wrapper(*args, **kwargs):
        try:
            return_data: tuple = func(*args, **kwargs)
            return Response(
                return_data[0],
                status=return_data[1] if len(return_data) > 1 else 200
            )
        except HttpFriendlyError as e:
            return Response({"message": e.message}, status=e.status_code)
        except AssertionError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            if ENV == 'dev':
                raise e
            else:
                return Response(
                    {"message": "Problemas ao processar sua requisição. Tente novamente mais tarde"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

    return wrapper
