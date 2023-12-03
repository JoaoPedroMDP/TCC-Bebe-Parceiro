#  coding: utf-8
from typing import List

from core.models import State, Country
from tests.utils.country_utils import create_country


def create_state(country: Country = None, name: str = "TES") -> State:
    if country is None:
        country = create_country()

    ac = State(name=name, country=country)
    ac.save()

    return ac


def create_n_states(name: str = "TEST_STATE", n: int = 1, country: Country = None) -> List[State]:
    if country is None:
        country = create_country()

    return [create_state(country, name + f"_{i}") for i in range(n)]


def delete_state(id: int) -> None:
    State.objects.filter(id=id).delete()


def delete_all_states() -> None:
    State.objects.all().delete()


def mark_states_as_disabled(states: List[State]) -> None:
    for state in states:
        state.enabled = False
        state.save()
