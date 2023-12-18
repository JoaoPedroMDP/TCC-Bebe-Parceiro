#  coding: utf-8
from typing import List

from core.models import MaritalStatus


def create_marital_status(name: str = "TES") -> MaritalStatus:
    marital_status = MaritalStatus(name=name)
    marital_status.save()

    return marital_status


def create_n_marital_statuses(name: str = "TEST_MARITAL_STATUS", n: int = 1) -> List[MaritalStatus]:
    return [create_marital_status(name + f"_{i}") for i in range(n)]


def delete_marital_status(id: int) -> None:
    MaritalStatus.objects.filter(id=id).delete()


def delete_all_marital_statuses() -> None:
    MaritalStatus.objects.all().delete()


def mark_marital_statuses_as_disabled(marital_statuses: List[MaritalStatus]) -> None:
    for marital_status in marital_statuses:
        marital_status.enabled = False
        marital_status.save()
