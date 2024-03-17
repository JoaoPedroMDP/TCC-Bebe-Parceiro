#  coding: utf-8
from abc import ABC
from typing import List

from rest_framework.views import APIView


class BaseView(APIView, ABC):
    groups: List[str]
