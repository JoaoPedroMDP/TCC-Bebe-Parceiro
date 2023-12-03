#  coding: utf-8
from typing import List

from core.models import State, City
from tests.utils.state_utils import create_state


def create_city(state: State = None, name: str = "TES") -> City:
    if state is None:
        state = create_state()

    ac = City(name=name, state=state)
    ac.save()

    return ac


def create_n_cities(name: str = "TEST_STATE", n: int = 1, state: State = None) -> List[City]:
    if state is None:
        state = create_state()

    return [create_city(state, name + f"_{i}") for i in range(n)]


def delete_city(id: int) -> None:
    City.objects.filter(id=id).delete()


def delete_all_cities() -> None:
    City.objects.all().delete()


def mark_cities_as_disabled(cities: List[City]) -> None:
    for city in cities:
        city.enabled = False
        city.save()
