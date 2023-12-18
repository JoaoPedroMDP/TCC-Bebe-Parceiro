#  coding: utf-8
from typing import List

from core.models import SocialProgram


def create_social_program(name: str = "TES") -> SocialProgram:
    social_program = SocialProgram(name=name)
    social_program.save()

    return social_program


def create_n_social_programs(name: str = "TEST_SOCIAL_PROGRAM", n: int = 1) -> List[SocialProgram]:
    return [create_social_program(name + f"_{i}") for i in range(n)]


def delete_social_program(id: int) -> None:
    SocialProgram.objects.filter(id=id).delete()


def delete_all_social_programs() -> None:
    SocialProgram.objects.all().delete()


def mark_social_programs_as_disabled(social_programs: List[SocialProgram]) -> None:
    for social_program in social_programs:
        social_program.enabled = False
        social_program.save()
