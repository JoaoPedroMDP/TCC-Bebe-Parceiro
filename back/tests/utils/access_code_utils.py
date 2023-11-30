#  coding: utf-8
from typing import List

from core.models import AccessCode
from core.services.access_code_service import AccessCodeService


def create_access_code(prefix: str = "TES"):
    ac = AccessCode(code=AccessCodeService.generate_code(prefix))
    ac.save()

    return ac


def create_n_access_codes(prefix: str = "TES", n: int = 1):
    return [create_access_code(prefix) for _ in range(n)]


def delete_access_code(id: int):
    AccessCode.objects.filter(id=id).delete()


def delete_all_access_codes():
    AccessCode.objects.all().delete()


def mark_codes_as_used(codes: List[AccessCode]):
    for code in codes:
        code.used = True
        code.save()