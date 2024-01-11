#  coding: utf-8
from typing import List

from core.cqrs.commands.volunteer_commands import CreateVolunteerCommand, PatchVolunteerCommand, \
    DeleteVolunteerCommand
from core.cqrs.queries.volunteer_queries import GetVolunteerQuery, ListVolunteerQuery
from core.models import Volunteer
from core.repositories.city_repository import CityRepository
from core.repositories.volunteer_repository import VolunteerRepository
from core.services import CrudService


class VolunteerService(CrudService):
    @classmethod
    def create(cls, command: CreateVolunteerCommand) -> Volunteer:
        # Verifica se a cidade passada é válida
        CityRepository.get(command.city_id)

        new_volunteer = VolunteerRepository.create(command.to_dict())

        # Para cada group_id passado, atribui o cargo
        for r_id in command.group_ids:
            new_volunteer.user.groups.add(r_id)

        return new_volunteer

    @classmethod
    def patch(cls, command: PatchVolunteerCommand) -> Volunteer:
        return VolunteerRepository.patch(command.to_dict())

    @classmethod
    def filter(cls, query: ListVolunteerQuery) -> List[Volunteer]:
        return VolunteerRepository.filter(**query.to_dict())

    @classmethod
    def get(cls, query: GetVolunteerQuery) -> Volunteer:
        return VolunteerRepository.get(query.id)

    @classmethod
    def delete(cls, command: DeleteVolunteerCommand) -> bool:
        return VolunteerRepository.delete(command.id)
