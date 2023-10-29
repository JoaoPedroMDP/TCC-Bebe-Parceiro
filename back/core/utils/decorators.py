#  coding: utf-8
from rest_framework import status
from rest_framework.response import Response

from core.utils.exceptions import WithHttpStatusCode


def endpoint(func):
    def wrapper(*args, **kwargs):
        try:
            return_data: tuple = func(*args, **kwargs)
            return Response(
                return_data[0],
                status=return_data[1] if len(return_data) > 1 else 200
            )
        except WithHttpStatusCode as e:
            return Response({"message": e.message}, status=e.status_code)
        except AssertionError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return wrapper
