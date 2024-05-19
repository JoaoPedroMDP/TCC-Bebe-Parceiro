#  coding: utf-8
import logging
from traceback import format_exc

from rest_framework import status
from rest_framework.response import Response

from config import DEV, ENV
from core.utils.exceptions import HttpFriendlyError


lgr = logging.getLogger(__name__)


def endpoint(func):
    def wrapper(*args, **kwargs):
        try:
            return_data: tuple = func(*args, **kwargs)
            return Response(
                return_data[0],
                status=return_data[1] if len(return_data) > 1 else 200
            )
        except HttpFriendlyError as e:
            lgr.error(format_exc())
            return Response({"message": e.message}, status=e.status_code)
        except AssertionError as e:
            lgr.error(format_exc())
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            lgr.error(format_exc())
            if ENV == DEV:
                raise e
            else:
                return Response(
                    {"message": "Problemas ao processar sua requisição. Tente novamente mais tarde"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

    return wrapper
