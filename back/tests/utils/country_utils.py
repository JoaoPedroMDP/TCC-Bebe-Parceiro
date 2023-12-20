#  coding: utf-8
from typing import List

from core.models import Country


def create_country(name: str = "TEST_COUNTRY") -> Country:
    country = Country(name=name)
    country.save()

    return country


def create_n_countries(name: str = "TEST_COUNTRY", n: int = 1) -> List[Country]:
    return [create_country(name + f"_{i}") for i in range(n)]


def delete_country(id: int) -> None:
    Country.objects.filter(id=id).delete()


def delete_all_countries() -> None:
    Country.objects.all().delete()


def mark_countries_as_disabled(countries: List[Country]) -> None:
    for country in countries:
        country.enabled = False
        country.save()
